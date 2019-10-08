#!/bin/sh
#PBS -l nodes=1:ppn=1
#PBS -n
#
ulimit -m `expr 60000000 / ${PBS_NUM_PPN}`
ulimit -v `expr 60000000 / ${PBS_NUM_PPN}`
source ~/.bashrc
#
export OMP_NUM_THREADS=4
#
cd $PBS_O_WORKDIR
#
python model_estimation.py
