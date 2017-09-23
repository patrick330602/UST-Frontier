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

def LZW(inp):
    temp = inp
    count = 0
    word_dict = []
    inp_list = list(inp)        # convert string to list
    for ch in inp_list:
        if ch not in word_dict:
            word_dict.append(ch)
    p = inp_list[0]
    inp_list.pop(0)
    for chrs in inp_list:
        tmp = p + chrs
        if tmp in word_dict:
            p = p + chrs
        else:
            word_dict.append(p+chrs)
            count += 1
            p = chrs
    count *= 12
    return count