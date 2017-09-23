def KnapsackFrac(v, w, W):
    order=[]
    order = [v/w for v, w in zip(v,w)]
    order.sort()
    order.reverse()
    n = len(order)
    index=0
    weight=0.0
    value=0.0
    while (weight < W) and (index < n):
        if weight + w[order[index]] <= W:
            weight = weight + w[order[index]]
            value = value + v[order[index]]
        else:
            fraction = (W - weight) / w[order[index]]
            weight = W
            value = value + v[order[index]] * fraction
        index=index+1
    return value
