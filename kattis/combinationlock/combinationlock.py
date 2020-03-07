
def cw(n1, n2):
    n1 += 40
    n1 -= n2
    n1 %= 40
    return n1

def ccw(n1, n2):
    n2 += 40
    n2 -= n1
    n2 %= 40
    return n2

while True:
    start, n1, n2, n3 = list(map(int, input().split()))
    if start == 0 and n1 == 0 and n2 == 0 and n3 == 0:
        break

    # 1 digit is 9 degrees
    number = 120 + cw(start, n1) + ccw(n1, n2) + cw(n2, n3)
    print(number * 9)
