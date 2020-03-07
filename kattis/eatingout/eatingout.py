m, a, b, c = list(map(int, input().split()))
if a + b + c <= 2 * m:
    print("possible")
else:
    print("impossible")
