import sys

while True:
  ## Each day
  dishes = dict()
  n = int(sys.stdin.readline())
  if n == 0:
    break
  for i in range(0, n):
    order = sys.stdin.readline().split()
    customer = order[0]
    for j in range(1, len(order)):
      if order[j] in dishes:
        dishes[order[j]].append(customer)
      else:
        dishes[order[j]] = [customer]
        
  ## Done all orders of the day
  arr = []
  for dish in dishes:
    arr.append(dish)
  arr.sort()
  
  ## Sorted arr
  for dish in arr:
    output = dish
    people = []
    for k in range(0, len(dishes[dish])):
      people.append(dishes[dish][k])
    
    people.sort()
      
    for k in range(0, len(people)):
      output += " " + people[k]
    print output
  print ''