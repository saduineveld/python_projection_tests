import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.interpolate import RectBivariateSpline

import BM_mod as BM

k = 2
alpha = 0.33
beta = 0.96

y = BM.prod(alpha,k)

print(k)
print(alpha)
print(y)

# Construct grid
nodes = 5
kss,css = BM.get_ss(alpha,beta)
lk_vec = np.linspace(math.log(kss)-0.2,math.log(kss)+0.2,nodes)

# Initial guess
lc_pol = math.log(css)+0.01*(lk_vec - math.log(kss))
print(lc_pol)

