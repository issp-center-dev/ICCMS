#!/bin/sh
#PBS -l nodes=1:ppn=28
#PBS -n

source ~/.bashrc
export OMP_NUM_THREADS=1
cd $PBS_O_WORKDIR

export PATH=$PATH:install_dir

bash install_dir/bin/GMXRC.bash

gmx_mpi_d grompp -f solution_run.mdp \
-c solution.gro \
-p etohsolution.top \
-o md.tpr

rm -f \#*

mpiexec -hostfile $PBS_NODEFILE  gmx_mpi_d mdrun --deffnm  md

