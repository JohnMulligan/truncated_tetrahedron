#!/bin/bash
#SBATCH --job-name=dihedral_angle_approx_sweeper
#SBATCH --partition=scavenge
#SBATCH --time=04:00:00
#SBATCH --export=ALL
#SBATCH --mail-user=jcm10@rice.edu
#SBATCH --mail-type=ALL
#SBATCH --array=0-49
module purge
module load  GCCcore/12.3.0
module load Python/3.11.3
pip3 install --user -r requirements.txt 

srun python3 find_approximate_folding_angles.py $1 $SLURM_ARRAY_TASK_ID $SLURM_ARRAY_TASK_COUNT