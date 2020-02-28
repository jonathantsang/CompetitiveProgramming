n = int(input())
items = sorted(list(map(int, input().split())), reverse=True)

dis = 0
for i in range(2, len(items), 3):
    dis += items[i]
print(dis)
