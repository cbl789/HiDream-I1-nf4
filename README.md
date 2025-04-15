# HiDream-I1-nf4 (Forked)

> **This is a fork of [azaneko/HiDream-I1-Full-nf4](https://github.com/azaneko/HiDream-I1-Full-nf4),**
> which is itself a fork of [HiDream-ai/HiDream-I1](https://github.com/HiDream-ai/HiDream-I1).
>
> This fork adds real-time progress updates, a streamlined Gradio UI, and other improvements for a better user experience.

---

## What's Different in This Fork?

- **Real-Time Progress Bar:**
  - Live progress updates during image generation, visible under the "Generate Image" button.
- **Clean Gradio UI:**
  - Only a single progress bar is shown (no duplicates in image/log areas).
  - **Remote Access:**
  - You can access the Gradio UI from other machines on your network (not just localhost).
- **Easy to Use:**
  - Just run the dashboard and enjoy a smooth, interactive experience.

---

## Installation

**This project uses a recent version of Gradio (v4+).**

Clone this repo and install dependencies:

```bash
git clone https://github.com/your-username/HiDream-I1-nf4.git
cd HiDream-I1-nf4
conda env create -f environment.yml
conda activate hdi1
pip install --upgrade gradio
```

Or install the package:

```bash
pip install hdi1 --no-build-isolation
pip install --upgrade gradio
```

---

## Running the Web Dashboard

```bash
bash start_gradio.sh
```

Or (if you want to run directly):

```bash
python -m hdi1.web
```

---

## Accessing the Web UI Remotely

By default, this fork starts Gradio with `server_name='0.0.0.0'`, allowing you to access the web UI from any device on your local network.

- Find your machine's local IP address (e.g., `192.168.1.42`).
- Open a browser on another device and go to:  
  `http://192.168.1.42:7860`

This makes it easy to use the dashboard from your phone, tablet, or another computer.

---

## Hardware Requirements

- **GPU:** NVIDIA >= Ampere (A100, H100, A40, RTX 3090, RTX 4090)
- **GPU RAM:** >= 16 GB
- **CPU RAM:** >= 16 GB

---

## Model Variants

| Name            | Min VRAM | Steps | HuggingFace                                                                                                                  |
|-----------------|----------|-------|------------------------------------------------------------------------------------------------------------------------------|
| HiDream-I1-Full | 16 GB    | 50    | 🤗 [Original](https://huggingface.co/HiDream-ai/HiDream-I1-Full) / [NF4](https://huggingface.co/azaneko/HiDream-I1-Full-nf4) |
| HiDream-I1-Dev  | 16 GB    | 28    | 🤗 [Original](https://huggingface.co/HiDream-ai/HiDream-I1-Dev) / [NF4](https://huggingface.co/azaneko/HiDream-I1-Dev-nf4)   |
| HiDream-I1-Fast | 16 GB    | 16    | 🤗 [Original](https://huggingface.co/HiDream-ai/HiDream-I1-Fast) / [NF4](https://huggingface.co/azaneko/HiDream-I1-Fast-nf4) |

---

## Features

- **Real-Time Progress Bar:**
  Users see a live progress bar under the "Generate Image" button during image generation.
- **Streamlined UI:**
  No redundant progress bars or logs—just a clean, modern interface.

---

## Credits

- Based on [azaneko/HiDream-I1-Full-nf4](https://github.com/azaneko/HiDream-I1-Full-nf4)
- Original project: [HiDream-ai/HiDream-I1](https://github.com/HiDream-ai/HiDream-I1) by HiDream-ai

---

## Changelog

- 2025-04-15: Added real-time progress bar, removed duplicate outputs, cleaned UI

---

For any issues or suggestions, please open an issue or pull request!

```

![Screenshot 2025-04-08 200120](https://github.com/user-attachments/assets/0c464033-5619-489d-b9de-fef5a7119cfc)

## License

The code in this repository and the HiDream-I1 models are licensed under [MIT License](./LICENSE).
