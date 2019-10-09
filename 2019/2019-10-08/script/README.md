# [memo] how to use hphi-modeling on sekirei

1. Use install scripts in sekirei folder.

2. Install combo by typing following command

    ``$ cd sekirei`` 
    ``$ sh install_combo.sh``

3. Move to ``tamura/hphi-modeling`` directory

   ``$ cd ../../tamura/hphi-modeling``

4. Uncomment line 31 in ``model_estimation.py``

    ``# hphi_cond["mpi_command"] = "mpijob"``
    -> ``hphi_cond["mpi_command"] = "mpijob"``

5. Use job script sample_hphi_sekirei.sh in sekirei folder.

   ``$ cp ../../script/sekirei/sample_hphi_sekirei.sh .``
   
   ``$ qsub sample_hphi_sekirei.sh``
   
