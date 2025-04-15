import torch
import gradio as gr
import logging
import io
import contextlib

from .nf4 import *

# Resolution options
RESOLUTION_OPTIONS = [
    "1024 × 1024 (Square, 1:1)",
    "768 × 1360 (Portrait, 9:16)",
    "1360 × 768 (Landscape, 16:9)",
    "880 × 1168 (Portrait, 3:4)",
    "1168 × 880 (Landscape, 4:3)",
    "1248 × 832 (Landscape, 3:2)",
    "832 × 1248 (Portrait, 2:3)"
]

# Parse resolution string to get height and width
def parse_resolution(resolution_str):
    return tuple(map(int, resolution_str.split("(")[0].strip().split(" × ")))


def gen_img_helper(model, prompt, res, seed, progress=gr.Progress()):
    global pipe, current_model
    # Suppress all print/log output so nothing is returned to Gradio outputs
    with contextlib.redirect_stdout(io.StringIO()):
        # 1. Check if the model matches loaded model, load the model if not
        if model != current_model:
            progress(0.1, desc=f"Unloading model {current_model}...")
            del pipe
            torch.cuda.empty_cache()
            progress(0.3, desc=f"Loading model {model}...")
            pipe, _ = load_models(model)
            current_model = model
        # 2. Generate image
        progress(0.6, desc="Generating image...")
        res = parse_resolution(res)
        image, seed_used = generate_image(pipe, model, prompt, res, seed, progress=progress)
        progress(1.0, desc="Done!")
    return image, seed_used


if __name__ == "__main__":
    logging.getLogger("transformers.modeling_utils").setLevel(logging.ERROR)
    
    # Initialize with default model
    print("Loading default model (fast)...")
    current_model = "fast"
    pipe, _ = load_models(current_model)
    print("Model loaded successfully!")

    # Create Gradio interface
    with gr.Blocks(title="HiDream-I1-nf4 Dashboard") as demo:
        gr.Markdown("# HiDream-I1-nf4 Dashboard")
        
        with gr.Row():
            with gr.Column():
                model_type = gr.Radio(
                    choices=list(MODEL_CONFIGS.keys()),
                    value="fast",
                    label="Model Type",
                    info="Select model variant"
                )
                
                prompt = gr.Textbox(
                    label="Prompt", 
                    placeholder="A cat holding a sign that says \"Hi-Dreams.ai\".", 
                    lines=3
                )
                
                resolution = gr.Radio(
                    choices=RESOLUTION_OPTIONS,
                    value=RESOLUTION_OPTIONS[0],
                    label="Resolution",
                    info="Select image resolution (aspect ratio shown)"
                )
                
                seed = gr.Number(
                    label="Seed (use -1 for random)", 
                    value=-1, 
                    precision=0
                )
                
                generate_btn = gr.Button("Generate Image")
                seed_used = gr.Number(label="Seed Used", interactive=False)
                
            with gr.Column():
                # Explicitly set format to PNG for output images
                output_image = gr.Image(label="Generated Image", type="pil", format="png")
        
        generate_btn.click(
            fn=lambda *args, **kwargs: gen_img_helper(*args, **kwargs)[:2],
            inputs=[model_type, prompt, resolution, seed],
            outputs=[output_image, seed_used],
            show_progress=True
        )

    # Allow remote access for older Gradio versions using server_name and server_port
    demo.launch(server_name='0.0.0.0', server_port=7860, share=False)
