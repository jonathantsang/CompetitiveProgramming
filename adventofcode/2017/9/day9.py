def Pal(s):
    ht = dict()
    for c in s:
        if c in ht:
            ht[c] += 1
        else:
            ht[c] = 1
    numodd = 0
    for k in ht.keys():
        if ht[k] % 2 == 1:
            numodd = 1
    return numodd < 2