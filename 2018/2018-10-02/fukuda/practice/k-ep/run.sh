#!/bin/sh
#PBS -l nodes=1:ppn=1
#PBS -l walltime=0:01:00
#
source ~/.bashrc
#
#export OMP_NUM_THREADS=1
#
cd $PBS_O_WORKDIR
#
./example.out ./ELSES_MATRIX_APF4686_20170505/ELSES_MATRIX_APF4686_A.mtx \
./ELSES_MATRIX_APF4686_20170505/ELSES_MATRIX_APF4686_B.mtx 2343 > output.txt

