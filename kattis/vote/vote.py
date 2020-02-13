import sys

T = int(sys.stdin.readline())
for _ in range(0, T):
    n = int(sys.stdin.readline())
    total = 0
    largest = -1
    winners = []
    for i in range(0, n):
        amt = int(sys.stdin.readline())
        total += amt
        if amt > largest:
            largest = amt
            winners = [i+1]
        elif amt == largest:
            winners.append(i+1)
    if len(winners) > 1:
        print("no winner")
    else:
        if largest > total // 2:
            print("majority winner {0}".format(winners[0]))
        else:
            print("minority winner {0}".format(winners[0]))
