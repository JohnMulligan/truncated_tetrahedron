#!/bin/bash
#SBATCH --job-name=dihedral
#SBATCH --partition=Scavenge
#SBATCH --ntasks=1
#SBATCH --time=05:00:00
#SBATCH --export=ALL
#SBATCH --mail-user=jcm10@rice.edu
#SBATCH --mail-type=ALL

module load GCCcore/8.3.0
module load Python/3.7.2
pip3 install networkx

python3 12 $SLURM_ARRAY_TASK_ID $SLURM_ARRAY_TASK_COUNT 50