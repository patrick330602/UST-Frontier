from decimal import Decimal

def KnapsackFrac(v, w, W):
    value = 0.0
    order = []
    n = len(v)
    for i in range(n):
        order.append(float(v[i] * 10000/w[i]))
    order, v, w = (list(t) for t in zip(*sorted(zip(order, v, w))))
    for i in range(n):
        wi = w[i]
        if wi >= W:
            a = int(v[i] * W)
            value += a
            return value
        else:
            b = int(v[i] * wi)
            value += b
            W -= wi
    return value