#!/bin/bash

# Activate the conda environment
source ~/miniconda3/etc/profile.d/conda.sh
conda activate hdi1

# Set CUDA device to 1
export CUDA_VISIBLE_DEVICES=1

# Launch the Gradio interface
python -m hdi1.web
