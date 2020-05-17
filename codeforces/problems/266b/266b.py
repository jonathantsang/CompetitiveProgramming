n, t = list(map(int, input().split()))
arr = list(input())

j = 0
while j < t:
    i = 0
    while i < len(arr)-1:
        if arr[i] == 'B' and arr[i+1] == 'G':
            arr[i], arr[i+1] = arr[i+1], arr[i]
            i += 1
        i += 1
    j += 1
print("".join(arr))
