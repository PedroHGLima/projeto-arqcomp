#!/bin/bash

#SBATCH --job-name=proj-arqcomp
#SBATCH --output=%x_%j.out

img_path=~/imgs/rootflow_latest.sif
singularity exec $img_path bash run_benchmark.sh
