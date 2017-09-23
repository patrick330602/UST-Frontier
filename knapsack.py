def KnapsackFrac(v, w, W):
    dictionary = {} #value: weight
    total_value = 0
    for i in range(len(v)):
        ratio = int(v[i]) / int(w[i])
        dictionary[ratio] = w[i]
    sorted_key = sorted(list(dictionary.keys()), reverse=True)
    for j in sorted_key:
        wi = dictionary[j]
        if wi >= W:
            total_value = total_value + int(j * W)
            return total_value
        else:
            total_value = total_value + int(j * wi)
            W -= wi
    return total_value
weight_max = 4
values = [1,3,5,2]
weight = [200, 240, 150, 140]
print(KnapsackFrac(values, weight, weight_max))