t = int(input())

v1 = [0, 1]
v2 = [0, 0]
v3 = [0, 0]

def calc(t):
    global v1
    global v2
    global v3
    for i in range(1, 21):
        for j in range(1, 21):
            for k in range(1, 21):
                # single, double, triple
                for l in range(1, 4):
                    for m in range(0, 4):
                        for n in range(0, 4):
                            val = i * l + j * m + k * n
                            # print(val, t)
                            if val == t:
                                v1 = [i, l]
                                v2 = [j, m]
                                v3 = [k, n]
                                return
calc(t)

names = {1: "single", 2:"double", 3:"triple"}

if v1[0] == 0:
    print("impossible")
else:
    print("{0} {1}".format(names[v1[1]], v1[0]))
    if v2[1] != 0:
        print("{0} {1}".format(names[v2[1]], v2[0]))
    if v3[1] != 0:
        print("{0} {1}".format(names[v3[1]], v3[0]))
