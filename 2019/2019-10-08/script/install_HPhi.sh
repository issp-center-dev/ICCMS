#!/bin/bash

wget https://github.com/issp-center-dev/HPhi/releases/download/v3.3.0/HPhi-3.3.0.tar.gz
tar xzvf HPhi-3.3.0.tar.gz
source /opt/intel/bin/compilervars.sh intel64
mkdir HPhi.build
cd HPhi.build
cmake -DCONFIG=intel ../HPhi-release/
make
