import sys

n1, n2 = list(sys.stdin.readline())[:-1], list(sys.stdin.readline())[:-1]
n1.reverse()
n2.reverse()
v1, v2 = [], []
for i in range(0, max(len(n1), len(n2))):
    if i >= len(n1):
        v2.append(n2[i])
    elif i >= len(n2):
        v1.append(n1[i])
    else:
        if n1[i] > n2[i]:
            v1.append(n1[i])
        elif n2[i] > n1[i]:
            v2.append(n2[i])
        else:
            v1.append(n1[i])
            v2.append(n2[i])
v1.reverse()
v2.reverse()
print(int("".join(v1))) if len(v1) > 0 else print("YODA")
print(int("".join(v2))) if len(v2) > 0 else print("YODA")
