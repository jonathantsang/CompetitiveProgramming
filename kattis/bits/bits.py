t = int(input())
for _ in range(0, t):
    n = input()
    best = 0
    for i in range(1, len(n)+1):
        c = bin(int(n[:i]))
        #print(n[:i])
        total = 0
        for d in c:
            if d == '1':
                total += 1
        best = max(best, total)
    print(best)
