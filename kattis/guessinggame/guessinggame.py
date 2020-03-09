
while True:
    # possible
    arr = [1 for i in range(0, 10)]

    # Game
    while True:
        # print(arr)
        possible = True
        val = int(input())
        if val == 0:
            exit(0)
        phrase, dir = input().split()
        if dir == "on":
            if arr[val-1] == 0:
                possible = False
            break
        elif dir == "high":
            for i in range(val-1, len(arr)):
                arr[i] = 0
        elif dir == "low":
            for i in range(0, val):
                arr[i] = 0
    if possible:
        print("Stan may be honest")
    else:
        print("Stan is dishonest")
