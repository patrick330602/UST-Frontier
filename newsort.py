import numpy as np

def sort(a):
#    N = 10000+10
#    c = [0]*(2*N+1)
#    for x in a:
#        c[x+10000] += 1
#    ret = []
#    for i, x in enumerate(c):
#        ret.extend([i-10000]*x)
#    return ret
    a = np.array(a)
    a += 10000
    a = np.repeat(np.arange(1+a.max()),np.bincount(a))-10000
    return a.tolist()
