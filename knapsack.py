from decimal import Decimal

def KnapsackFrac(v, w, W):
    value = 0.0
    order = []
    n = len(v)
    for i in range(n):
        order.append(float(v[i] * 10000/w[i]))
    order, v, w =zip(*sorted(zip(order, v, w)))
    for r in range(n):
        wi = w[r]
        if wi >= W:
            value = value + int(order[r] /10000 * W)
            return value
        else:
            value = value + int( order[r] /10000* wi)
            W = W - wi
    return value

a = 4
b = [1,3,5,2]
c = [200, 240, 150, 140]
print(KnapsackFrac(c,b,a))