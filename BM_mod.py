# BM model module

import numpy as np

def get_res(alpha,beta,lk_vec,pol_old,lc_pol):
    ct = np.exp(lc_pol)
    kn = knext(alpha,np.exp(lk_vec),ct)
    lcn = pol_old(np.log(kn))
    Rn = alpha*kn**(alpha-1)
    RES = beta*np.exp(-lcn)*Rn*ct-1
    return RES



def get_ss(alpha,beta):
    kss = (alpha*beta)**(1/(1-alpha))
    css = kss**alpha - kss
    return kss,css


def marg_ut(nu,cc):
    dudc = cc**-nu
    return dudc

def knext(alpha,kt,ct):
    kn = prod(alpha,kt) - ct
    return kn


def cons(alpha,kt,kn):
    cc = prod(alpha,kt) - kn
    return cc

def prod(alpha,kk): 
    yy = kk**alpha
    return yy
