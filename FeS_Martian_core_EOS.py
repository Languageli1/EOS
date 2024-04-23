# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 21:57:42 2024

@author: lwj
"""
import numpy as np

P_param0=np.array([ 8.38887520e+01,  0.00000000e+00, -4.06101839e+01,  2.37438774e-03,
        4.62652625e+00,  2.26901272e-04,  1.87440346e-07])

def P_fit0(rho,T,P_param0):
    # rho is density, range [6.1,7.5] g/cm3; 
    # T is temperature, range [1600,2600] K; 
    # P is pressure, range [15,49] GPa;
    return P_param0[0] + P_param0[1] + P_param0[2]*rho + P_param0[3]*T + \
        P_param0[4]*rho*rho + P_param0[5]*rho*T + P_param0[6]*T*T 

#%%
P_param1=[ 5.40528557e+02,  0.00000000e+00, -7.26243043e+01,  5.42748223e-03,
        2.46141707e+00, -1.23887453e-04,  1.87440365e-07]

def P_fit1(V,T,P_param1):
    # V is volume per atom of Fe3S, range [10.9-13.2]A3; 
    # T is temperature, [1600,2600] K; 
    # P is pressure, [15,49] GPa;
    return P_param1[0] + P_param1[1] + P_param1[2]*V + P_param1[3]*T + \
        P_param1[4]*V*V + P_param1[5]*V*T + P_param1[6]*T*T 
