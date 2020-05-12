for testcase in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
 
    special = [False] * (n + 1)
    for i in range(n):
        s = arr[i]
        for j in range(i + 1, n):
            s += arr[j]
            if s > n:
                break
            special[s] = True
 
    print(sum(1 for x in arr if special[x]))