import numpy as np
# import math
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

import BM_mod as BM

# Parameters
alpha = 0.33
beta = 0.96

max_err = 1e-10

# Construct grid
nodes = 5
kss,css = BM.get_ss(alpha,beta)
lk_vec = np.linspace(np.log(kss)-0.2,np.log(kss)+0.2,nodes)

# Initial guess
#lc_pol = np.log(css)+0.01*(lk_vec - np.log(kss))
lc_pol = np.log(1-alpha*beta) + alpha*lk_vec

# Transfer policy to spline:
pol_old = CubicSpline(lk_vec,lc_pol)

# Test residual function
RES = BM.get_res(alpha,beta,lk_vec,pol_old,lc_pol)
print(RES)

# Solve residual function, until max residual is smaller than tolerance