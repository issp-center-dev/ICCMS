#FC = mpif90
#MACRO_PREFIX = -D
#CPPFLAG = -cpp
#FFLAGS = -O3 -Wall -fopenmp
#LDFLAGS = $(FFLAGS)
#LIBS = -lscalapack -llapack -lblas -lgomp
#WNO_UNUSED_DUMMY_ARGUMENT_FLAG = -Wno-unused-dummy-argument
#
FC = mpif90
MACRO_PREFIX = -D
CPPFLAG = -cpp
FFLAGS = -O2 -warn all -fopenmp -xHost -mkl=parallel -I/home/public/ -I/home/public/include/elpa_openmp-2014.06.001/modules/
LDFLAGS = $(FFLAGS)
WITH_EIGENEXA=1
WITH_ELPA=1
LIBS = -L/home/public/lib/ -L/home/public/lib/ -lelpa_openmp -lEigenExa -lmkl_scalapack_lp64 -lmkl_blacs_openmpi_lp64 -liomp5 -lpthread -lm -ldl
WNO_UNUSED_DUMMY_ARGUMENT_FLAG = -Wno-unused-dummy-argument
