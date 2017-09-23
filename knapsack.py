def KnapsackFrac(v, w, W):
    weight = 0.0
    value = 0.0
    knapsack = []
    index = 0
    order = []
    n = len(v)
    for i in range(n):
        order.append(float(v[i] * 10000/w[i]))
    order, v, w =zip(*sorted(zip(order, v, w)))
    
    while (weight < W) and (index < n):
        if weight + w[order[index]] <= W:
            knapsack.append((order[index], 1.0))
            weight = weight + w[order[index]]
            value = value + v[order[index]]
        else:
            fraction = (W - weight) / w[order[index]]
            knapsack.append((order[index], fraction))
            weight = W
            value = value + v[order[index]] * fraction
        index = index + 1
    return value

#a = 5
#b = [1,3,5,2]
#c = [200, 240, 150, 140]
#print(KnapsackFrac(c,b,a))