from collections import defaultdict

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')

def check(L,C,MID,FINAL): # attempt to fit "MID" number of cars
    cars = C[:MID]
    cars = [(v,i) for i,v in enumerate(cars)]
    cars.sort()

    l = 0
    r = 0
    car_amt = 0
    side = defaultdict(None) # index -> port or starboard
    for i in range(MID-1,-1,-1):
      if l+cars[i][0] > L and r+cars[i][0] > L:
          break
      if l > r:
          side[cars[i][1]] = "starboard"
          r += cars[i][0]
          car_amt += 1
      else:
          side[cars[i][1]] = "port"
          l += cars[i][0]
          car_amt += 1
    #print(car_amt)

    if not FINAL:
        return car_amt if car_amt == MID else 0
    else:
        for i in range(MID):
            print(side[i])

def solve(L,C):
    # greedy by one side
    l = 0
    r = 0
    ans = []
    for car in C:
        if car+l > L and car+r > L:
            break
        if car+l < L:
            l += car
            ans.append("port")
        else: # try to fit on right side
            r += car
            ans.append("starboard")

    #print(best)

    #check(L,C,best,True)

    # balanced?
    l = 0
    r = 0
    ans2 = []
    for car in C:
        if car+l > L and car+r > L:
            break
        if l < r:
            l += car
            ans2.append("port")
        else: # try to fit on right side
            r += car
            ans2.append("starboard")

    if len(ans) > len(ans2):
        print(len(ans))
        for v in ans:
            print(v)
    else:
        print(len(ans2))
        for v in ans2:
            print(v)


L = rri()
L *= 100 # convert m->cm
cars = []

a = rri()
while a != 0:
    #print(a)
    cars.append(a)
    a = rri()

solve(L,cars)
