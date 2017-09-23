def KnapsackFrac(v, w, W):
    dictionary = {} #value: weight
    total_value = 0
    for i in range(len(v)):
        rt = int(v[i]) / int(w[i])
        dt[rt] = w[i]
    sk = sorted(list(dt.keys()), reverse=True)
    for j in sk:
        wi = dt[j]
        if wi < W:
            total_value = total_value + int(j * wi)
            W -= wi
        else:
            total_value = total_value + int(j * W)
            return total_value
    return total_value