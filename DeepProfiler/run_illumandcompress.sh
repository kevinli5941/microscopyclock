#!/bin/bash

#SBATCH -c 4
#SBATCH -t 5-00:00
#SBATCH -p gpu_quad
#SBATCH  -o ../logs/%x.out
#SBATCH --gres=gpu:1,vram:40G
#SBATCH --mem 240G
#SBATCH -J preprocessing1

module load gcc/9.2.0
module load cuda/11.7

conda init bash
source ~/.bashrc
conda activate microscopymodel

python3 deepprofiler --root=/n/data1/hms/dbmi/zitnik/lab/users/kel331/microscopyclock --config=training_profiling.json prepare