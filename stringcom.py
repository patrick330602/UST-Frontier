def RLE(inp):
    temp = inp
    count = -1
    countlist = []
    inp_list = list(inp)        # convert string to list
    for ch in inp_list:
        if temp != ch:          # when letter do not match
            temp = ch
            count += 1
            countlist.append(1)
        else:
            countlist[count] += 1
    count += 1                  # add a missing count
    for i in countlist:
        if i != 1:
            count += len(str(i))
    count *= 8
    return count


