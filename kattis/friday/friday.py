import sys

T = int(sys.stdin.readline())

def run(d, m, months):
  days = m
  current_day = 0
  current_month = 0
  count = 0
  
  while days > 0:
    if months[current_month] > 12 and (current_day + 12) % 7 == 5:
      count += 1
    days -= months[current_month]
    current_day = (current_day + months[current_month]) % 7
    current_month += 1
  
  print(count)  

for i in range(0, T):
  md = list(map(int, sys.stdin.readline().split()))
  d = md[0]
  m = md[1]
  months = list(map(int, sys.stdin.readline().split()))
  run(d, m, months)