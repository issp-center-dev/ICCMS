# Fortran compiler and its options
FC = mpif90
FFLAGS = -O3

# MUMPS
MUMPSPATH = 
MUMPSFLAGS = -L/home/public/lib -ldmumps -lmumps_common 

# METIS
METISPATH = 
METISFLAGS = -lmetis

# PORD (MUMPS built-in library)
PORDPATH = 
PORDFLAGS = -lpord

# MPI for MUMPS (Sequential version of MUMPS requires MPI)
MPIPATH = 
MPIFLAGS =  -lmkl_scalapack_lp64 -lmkl_blacs_openmpi_lp64 -liomp5 -lpthread -lm -ldl

# LAPACK
LAPACKPATH = 
LAPACKFLAGS =

# BLAS
BLASPATH = 
BLASFLAGS = -mkl

OTHERFLAGS = -lpthread -lm

LIBS = $(MUMPSFLAGS) $(METISFLAGS) $(PORDFLAGS) $(MPIFLAGS) $(LAPACKFLAGS) $(BLASFLAGS) $(OTHERFLAGS)

# For MUMPS
INCMPI = set_path_if_necessary_/MUMPS_5.0.1/libseq
INCMUMPS = set_path_if_necessary_/MUMPS_5.0.1/include
INCLUDES = -I. -I$(INCMPI) -I$(INCMUMPS)
