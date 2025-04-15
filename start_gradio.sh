#!/bin/bash

LOGFILE="gradio_server.log"

# Activate the conda environment
echo "[INFO] Activating conda environment: hdi1"
source ~/miniconda3/etc/profile.d/conda.sh
conda activate hdi1

# Show Python and Gradio version
echo "[INFO] Python version: $(python --version)"
echo "[INFO] Gradio version: $(python -c 'import gradio; print(gradio.__version__)')"

# Set CUDA device to 1
echo "[INFO] Setting CUDA_VISIBLE_DEVICES=1"
export CUDA_VISIBLE_DEVICES=1

# Show IP address for remote access
echo "[INFO] Local IP address: $(hostname -I | awk '{print $1}')"
echo "[INFO] Web UI will be available at http://$(hostname -I | awk '{print $1}'):7860"

# Launch the Gradio interface
echo "[INFO] Launching Gradio interface..."
python -m hdi1.web
