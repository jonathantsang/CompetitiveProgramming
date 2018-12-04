import math
import sys
import datetime, time

lines = []
for line in sys.stdin:
  lines.append(line)
  
lines.sort()

guards = dict()
guard = 0
times = []
for line in lines:
  arr = line.split(' ')
  if arr[2] == "Guard":
    guard = int(arr[3][1:])
    if guard not in guards:
      guards[guard] = 0
  elif arr[2] == "falls":
    p1 = list(map(int, arr[0][1:].split('-')))
    p2 = list(map(int, arr[1][:len(arr[1])-1].split(':')))
    ss = (datetime.datetime(p1[0]+490,p1[1],p1[2], p2[0],p2[1]))
    sleepstart = time.mktime(ss.timetuple())
    times.append(['f', p2[0], p2[1], guard])
  elif arr[2] == "wakes":
    p1 = list(map(int, arr[0][1:].split('-')))
    p2 = list(map(int, arr[1][:len(arr[1])-1].split(':')))
    se = (datetime.datetime(p1[0]+490,p1[1],p1[2], p2[0],p2[1]))
    sleepend = time.mktime(se.timetuple())
    guards[guard] += (sleepend - sleepstart)
    times.append(['w', p2[0], p2[1], guard])
  
bestforall = 0
b = 0
mina = 0
for g in guards:
  mins = dict() ## 0 to 59
  for i in range(0, 60):
    mins[i] = 0
  
  # print(times)
  i = 0
  while(i < len(times)):
    ## Fall
    if int(times[i][3]) == int(g):
      sleepM = int(times[i][2])
      sleepH = int(times[i][1])
      wakeM = int(times[i+1][2])
      wakeH = int(times[i+1][1])
      # print(sleepH, sleepM, "n", wakeH, wakeM)
      while(sleepH < wakeH or ( sleepH == wakeH and sleepM < wakeM)):
        mins[sleepM] += 1
        sleepM += 1
        if sleepM == 60:
          sleepM = 0
          sleepH += 1
      i += 2
    else:
      i+=1
  
  best = 0
  a = 0
  for i in range(0, 60):
    if best < mins[i]:
      a = i
      best = mins[i]
  
  # check a with rest of guards
  if best > bestforall:
    b = g
    mina = a
    bestforall = best

print(b, mina, bestforall)