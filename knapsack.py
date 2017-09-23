import decimal
def KnapsackFrac(v, w, W):
    value = 0.0000000000
    order=[]
    n = len(v)
    for j in range(n):
        order.append(decimal.Decimal(v[j])/decimal.Decimal(w[j]))
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

weight_max = 4
values = [1,3,5,2]
weight = [200, 240, 150, 140]
print(KnapsackFrac(values, weight, weight_max))