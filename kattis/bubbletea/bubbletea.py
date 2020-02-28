import sys

teas = int(sys.stdin.readline())
tea_prices = list(map(int, sys.stdin.readline().split()))
toppings = int(sys.stdin.readline())
top_prices = list(map(int, sys.stdin.readline().split()))

mix = {} # key: tea index i -> [possible idx for toppings]

for i in range(0, teas):
    line = list(map(int, sys.stdin.readline().split()))
    mix[i] = line[1:]

money = int(sys.stdin.readline())

cheapest = float('inf')
for i, tea_price in enumerate(tea_prices):
    for topping in mix[i]:
        cheapest = min(cheapest, tea_price + top_prices[topping-1])

print("{0}".format(max(0, (money - cheapest) // cheapest)))
