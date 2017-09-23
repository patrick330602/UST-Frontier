import operator
def KnapsackFrac(v, w, W):
    value = 0
    order=[]
    order = [v/w for v, w in zip(v,w)]
    dict_order = zip(order, w)
    sorted(dict_order, key=lambda x: x[0])
        for i in dict_order:
            wi = i[1]
            if wi >= W:
                a = int(i[0] * W)
                value += a
                return value
            else:
                b = int(i[0] * wi)
                value += b
                W -= wi
    return value
