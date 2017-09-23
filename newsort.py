def sort(a):
    N = 10000+10
    c = [0]*(2*N+1)
    for x in a:
        c[x+10000] += 1
    ret = []
    for i, x in enumerate(c):
        ret.extend([i-10000]*x)
    return ret
