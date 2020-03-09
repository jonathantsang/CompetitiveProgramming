
while True:
    v = input().split()
    if len(v) == 1 and v[0] == str(0):
        break
    front = list(map(int, input().split()))
    rear = list(map(int, input().split()))
    ratios = []
    for ft in front:
        for fr in rear:
            ratios.append(fr / ft)
    ratios.sort()
    spreads = []
    for i in range(1, len(ratios)):
        spreads.append(ratios[i] / ratios[i-1])
    #print(spreads)
    print("{:.2f}".format(max(spreads)))
