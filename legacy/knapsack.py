def KnapsackFrac(v, w, W):
    order = bubblesortByRatio(v,w)
    weight = 0.0
    value = 0.0
    knapsack = []
    n = len(v)
    index = 0
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

def bubblesortByRatio(list1, list2):
    n=len(list1)
    order = list(range(n))
    for i in range(n - 1, 0, -1): 
        for j in range(0, i):
            if ((1.0 * list1[order[j]])*list2[order[j+1]] < (1.0 * list1[order[j+1]])*list2[order[j]]):
                temp = order[j]
                order[j] = order[j+1]
                order[j+1] = temp
    return order
