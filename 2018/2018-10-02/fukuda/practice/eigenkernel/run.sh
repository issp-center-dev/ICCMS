#!/bin/sh
#PBS -l nodes=1:ppn=4
#PBS -l walltime=0:01:00
#
source ~/.bashrc
#
#export OMP_NUM_THREADS=1
#
cd $PBS_O_WORKDIR
#
mpiexec -hostfile $PBS_NODEFILE ../bin/eigenkernel_app \
 -s general_scalapack ELSES_MATRIX_BNZ30_A.mtx ELSES_MATRIX_BNZ30_B.mtx
