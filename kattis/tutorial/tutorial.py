import math

m, n, t = list(map(int, input().split()))

val = 0

if t == 1:
    val = 1
    for i in range(n, 0, -1):
        val *= i
        if val > m:
            break
elif t == 2:
    val = 2**n
elif t == 3:
    val = n**4
elif t == 4:
    val = n**3
elif t == 5:
    val = n**2
elif t == 6:
    val = n * math.log(n, 2)
elif t == 7:
    val = n

print("AC") if val <= m else print("TLE")
