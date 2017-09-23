import numpy as np

def KnapsackFrac(v, w, W):
    p = np.empty(len(v))
    for i in range(len(v)):
        p[i] = -v[i]/w[i]
    idx = np.argsort(p)
    val = 0
    for i in idx:
        use_w = min(W, w[i])
        W -= use_w
        val += v[i]/w[i]*use_w
        if W<=0: break
    return int(val)


#a = 5
#b = [1,3,5,2]
#c = [200, 240, 150, 140]
#print(KnapsackFrac(c,b,a))