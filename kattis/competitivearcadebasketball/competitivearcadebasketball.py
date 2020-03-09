n, p, m = list(map(int, input().split()))
names = {}
one_win = False
for _ in range(0, n):
    names[input().strip()] = [0, 0]
for _ in range(0, m):
    name, points = input().split()
    points = int(points)
    names[name][0] += points
    if names[name][0] >= p and names[name][1] == 0:
        print("{0} wins!".format(name))
        names[name][1] = 1
        one_win = True
if not one_win:
    print("No winner!")
