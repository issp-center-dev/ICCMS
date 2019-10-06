#In
import numpy as np
import cPickle as pickle
import scipy
import combo
import os
import urllib
import matplotlib.pyplot as plt
#matplotlib inline

#In

import hphi_io as hphi

hphi_cond = {}
hphi_cond["path_hphi"] = "./HPhi"
hphi_cond["path_input_file"] = "./stan.in"
HPhi_calc = hphi.calc_mag(hphi_cond)


#In
#Create candidate
window_num=20

J1_lower=0.0
J1_upper=2.0

J2_lower=0.0
J2_upper=2.0

J3_lower=0.0
J3_upper=2.0

X=[]

for i in range(window_num+1):
    for j in range(window_num+1):
       for k in range(window_num+1):

          X.append([round(J1_lower+(J1_upper-J1_lower)/window_num*i,3),
          round(J2_lower+(J2_upper-J2_lower)/window_num*j,3),
          round(J3_lower+(J3_upper-J3_lower)/window_num*k,3)])


X=np.array(X)



#In

#target magnetization
input_dict = {}
input_dict["J0"] = 1.0
input_dict["J0'"] = 0.5
input_dict["J0''"] = 0.3
energy_list = HPhi_calc.get_energy_by_hphi(input_dict)

magnetic_field=[0.01*num for num in range(300)]

target=[]

for H in magnetic_field:
    target.append(HPhi_calc.get_mag(energy_list, H))


fig = plt.figure(figsize=(10, 6))
plt.plot(magnetic_field,target,'.',label="target")
plt.xlabel("Magnetic field")
plt.ylabel("Magnetization")
plt.legend(loc='lower right')
plt.show()





#In
# Load the data.
# X is the N x d dimensional matrix. Each row of X denotes the d-dimensional feature vector of search candidate.
# t is the N-dimensional vector that represents the corresponding negative energy of search candidates.
# ( It is of course unknown in practice. )


# Normalize the mean and standard deviation along the each column of X to 0 and 1, respectively
X_normalized = combo.misc.centering( X )



#In
# Declare the class for calling the simulator.
# In this tutorial, we simply refer to the value of t.
# If you want to apply combo to other problems, you have to customize this class.
class simulator:

    def __init__( self ):

        pass

    def __call__( self, action ):
    
        input_dict = {}
        input_dict["J0"] = X[action][0][0]
        input_dict["J0'"] = X[action][0][1]
        input_dict["J0''"] = X[action][0][2]
        energy_list = HPhi_calc.get_energy_by_hphi(input_dict)


        delta_m=0.0

        for num in range(300):
            delta_m=delta_m+(HPhi_calc.get_mag(energy_list, magnetic_field[num])-target[num])**2


        return -delta_m



#In
# Design of policy

# Declaring the policy by
policy = combo.search.discrete.policy(test_X=X_normalized)
# test_X is the set of candidates which is represented by numpy.array.
# Each row vector represents the feature vector of the corresponding candidate

# set the seed parameter
policy.set_seed( 111 )



#In[]

# If you want to perform the initial random search before starting the Bayesian optimization,
# the random sampling is performed by

res = policy.random_search(max_num_probes=20, simulator=simulator())
# Input:
# max_num_probes: number of random search
# simulator = simulator
# output: combo.search.discreate.results (class)


# single query Bayesian search
# The single query version of COMBO is performed by
res = policy.bayes_search(max_num_probes=80, simulator=simulator(), score='TS',
                                                  interval=20, num_rand_basis=5000)

# Input
# max_num_probes: number of searching by Bayesian optimization
# simulator: the class of simulator which is defined above
# score: the type of aquision funciton. TS, EI and PI are available
# interval: the timing for learning the hyper parameter.
#               In this case, the hyper parameter is learned at each 20 steps
#               If you set the negative value to interval, the hyper parameter learning is not performed
#               If you set zero to interval, the hyper parameter learning is performed only at the first step
# num_rand_basis: the number of basis function. If you choose 0,  ordinary Gaussian process runs



#In

best_fx, best_action = res.export_all_sequence_best_fx()

#estimated magnetization
input_dict = {}
input_dict["J0"] = X[int(best_action[-1])][0]
input_dict["J0'"] = X[int(best_action[-1])][1]
input_dict["J0''"] = X[int(best_action[-1])][2]
energy_list = HPhi_calc.get_energy_by_hphi(input_dict)

estimated=[]

for H in magnetic_field:
    estimated.append(HPhi_calc.get_mag(energy_list, H))


fig = plt.figure(figsize=(10, 6))
plt.plot(magnetic_field,target,'.',label="target")
plt.plot(magnetic_field,estimated,'.',label="estimated")
plt.xlabel("Magnetic field")
plt.ylabel("Magnetization")
plt.legend(loc='lower right')
plt.show()


print ''
print 'Estimated model parameter'
print 'J1=',X[int(best_action[-1])][0]
print 'J2=',X[int(best_action[-1])][1]
print 'J3=',X[int(best_action[-1])][2]
print ''
print ''



#In

# The result of searching is summarized in the class combo.search.discrete.results.history()
# res.fx: observed negative energy at each step
# res.chosed_actions: history of choosed actions
# fbest, best_action= res.export_all_sequence_best_fx(): current best fx and current best action
#                                                                                                   that has been observed until each step
# res.total_num_search: total number of search
print 'f(x)='
print res.fx[0:res.total_num_search]
#best_fx, best_action = res.export_all_sequence_best_fx()
print 'current best'
print best_fx
print 'current best action='
print best_action
print 'history of chosed actions='
print res.chosed_actions[0:res.total_num_search]
        
