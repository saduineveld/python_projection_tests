# BM model module


def marg_ut(nu,cc):
    dudc = cc**-nu
    return dudc

def knext(alpha,kt,cc):
    kn = prod(alpha,kt) - cc
    return kn


def cons(alpha,kt,kn):
    cc = prod(alpha,kt) - kn
    return cc

def prod(alpha,kk): 
    yy = kk**alpha
    return yy
