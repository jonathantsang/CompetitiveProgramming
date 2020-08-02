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
    N = len(C)
    lo = 0
    hi = N
    best = 0

    while lo <= hi:
        mid = lo+hi>>1
        if mid == 0:
            print(0)
            return
        #print(lo,hi,mid)

        # allow mid cars in
        amt = check(L,C,mid,False)
        if amt < best:
            hi = mid-1
        else:
            lo = mid+1
        best = max(best, amt)

    print(best)
    check(L,C,best,True)

L = rri()
L *= 100 # convert m->cm
cars = []

a = rri()
while a != 0:
    #print(a)
    cars.append(a)
    a = rri()

solve(L,cars)
