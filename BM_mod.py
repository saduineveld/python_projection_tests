# BM model module

def get_res(alpha,beta,lk_vec,pol_old,lc_pol)
    kt = math.exp(lk_vec)
    kn = knext(alpha,kt,lc_pol)
    lkn = math.log(kn)
    lcn = pol_old(lkn)
    Rn = alpha*kn^(alpha-1)
    RES = lc_pol
    return RES



def get_ss(alpha,beta):
    kss = (alpha*beta)**(1/(1-alpha))
    css = kss**alpha - kss
    return kss,css


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
