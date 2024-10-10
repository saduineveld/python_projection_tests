import numpy as np
# import math
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
from scipy.optimize import fsolve
#from scipy.sparse import eye
#from scipy.sparse import csr_matrix

import BM_mod as BM

# Parameters
alpha = 0.33
beta = 0.96

max_error = 1e-10

# Construct grid
nodes = 5
kss,css = BM.get_ss(alpha,beta)
lk_vec = np.linspace(np.log(kss)-0.2,np.log(kss)+0.2,nodes)

# Analtical solution
lc_ana = np.log(1-alpha*beta) + alpha*lk_vec
print(lc_ana)
pol_ana = CubicSpline(lk_vec,lc_ana)

# Initial guess
lc_old = np.log(css)+0.01*(lk_vec - np.log(kss))

# Transfer policy to spline:
pol_old = CubicSpline(lk_vec,lc_old)

# Test residual function
#RES = BM.get_res(alpha,beta,lk_vec,pol_old,lc_old)
#print(RES)

def equations(lc_pol,alpha,beta,lk_vec,pol_old):
    RES = BM.get_res(alpha,beta,lk_vec,pol_old,lc_pol)
    return RES


# Solve residual function, until max residual is smaller than tolerance. No Jacobian pattern specified
#while True:
#    lc_new = fsolve(equations, lc_old, args=(alpha, beta, lk_vec, pol_old))  
#    print(lc_new)  
#    if np.all(np.abs(lc_new - lc_old) < max_error):
#        break
#    lc_old = lc_new  # update lc_old
#    pol_old = CubicSpline(lk_vec, lc_old)  # update pol_old

# OLD SUGGESTION:
#def sparse_jacobian(lc_old, *args):
#    rows = [i for i in range(len(lc_old))]
#    cols = [i for i in range(len(lc_old))]
#    data = [1] * len(lc_old)  # dummy values, not actually used
#    return csr_matrix((data, (rows, cols)), shape=(len(lc_old), len(lc_old)))
def sparse_jacobian(lc_old, *args):
    return np.eye(len(lc_old))


while True:
    lc_new = fsolve(equations, lc_old, fprime=sparse_jacobian, args=(alpha, beta, lk_vec, pol_old), xtol=1e-12)
    print(lc_new)
    lc_old = lc_new  # update lc_old
    pol_old = CubicSpline(lk_vec, lc_old)  # update pol_old
    RES = equations(lc_old,alpha,beta,lk_vec,pol_old)
    print(RES)
    if np.all(np.abs(RES) < max_error):
        break
    
    
