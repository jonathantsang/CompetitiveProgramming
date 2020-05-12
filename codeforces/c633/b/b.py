import collections

t = int(input())

for _ in range(0, t):
    l = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    ans = collections.deque()
    turns = [0, 1] # smallest then largest
    j = 0
    lidx = len(arr)-1
    sidx = 0
    while lidx >= sidx:
        j %= 2
        if turns[j] == 0:
            ans.appendleft(arr[sidx])
            sidx += 1
            j += 1
        else:
            ans.appendleft(arr[lidx])
            lidx -= 1
            j += 1

    print(" ".join(list(map(str, ans))))
