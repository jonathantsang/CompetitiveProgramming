n, m = list(map(int, input().split()))
tasks = sorted(list(map(int, input().split())))
intervals = sorted(list(map(int, input().split())))

complete = 0
i = 0 # tasks
j = 0 # intervals
while j < len(intervals):
    if tasks[i] <= intervals[j]:
        i += 1
        j += 1
        complete += 1
    else:
        j += 1

print(complete)
