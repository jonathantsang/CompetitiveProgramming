first = True

while True:
    n = int(input())
    if n == 0:
        break
    elif not first:
        print('')
    first = False
    times = []
    for _ in range(0, n):
        time = input().split()
        # 12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 -> 12,
        h = int(time[0].split(':')[0])
        if h == 12:
            h = 0
        m = int(time[0].split(':')[1])
        tm = h * 60 + m
        if time[1] == "p.m.":
            tm += 12 * 60
        time.insert(0, tm)
        times.append(time)
    times.sort()
    for t in times:
        print(t[1], t[2])
