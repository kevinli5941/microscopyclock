#!/bin/bash

#SBATCH -c 8
#SBATCH -t 2:00:00
#SBATCH -p short
#SBATCH  -o logs/%x.out
#SBATCH --mem 20G
#SBATCH -J combine_highmem_full_attempt

module load gcc/9.2.0
module load cuda/11.7
module load java/jdk-17.0.7

conda init bash
source ~/.bashrc
conda activate cellprofiler

python3 segmentation.py