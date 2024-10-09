import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import RectBivariateSpline

import BM_mod

k = 2
alpha = 0.33

y = BM_mod.prod(alpha,k)

print(k)
print(alpha)
print(y)
