#! /usr/bin/python3

import sys
import math

calories = [0,0,0,0,0]

# Fat is 9C/g
# protein, sugar, starch 4C/g
# alcohol 7C/g

# 2000 calorie diet
# 10% is 200 calories
prev = False

for line in sys.stdin:
  # print("total", calories)
  if line == '-\n':
    if prev == True:
      break
    # calculate
    print(str(int(round((float(calories[0]) / float(sum(calories))) * 100))) + '%')
    calories = [0,0,0,0,0]
    prev = True
    
  else:
    prev = False

    inter = [0,0,0,0,0]
    
    fpssa = list(line[0:-1].split(' '))
    indices = []
    total = 0
    percentage_sum = 0
    for i in range(0, len(fpssa)):  
      if fpssa[i][-1] == 'g':
        cals = float(fpssa[i][0:-1])
        if i == 0:
          cals *= 9
        elif i == 4:
          cals *= 7
        else:
          cals *= 4
        inter[i] += cals
        total += cals
        
      if fpssa[i][-1] == 'C':
        cals = float(fpssa[i][0:-1])
        inter[i] += cals
        total += cals
        
      if fpssa[i][-1] == '%':
        percentage_sum += float(fpssa[i][0:-1])
        indices += [i]
    # normalize total to 100%
    total = total / (1 - percentage_sum / 100)
    
    for i in indices:
      # total * percentage%
      inter[i] = total * float(fpssa[i][0:-1]) / 100
    
    # copy over
    # print(inter)
    for i in range(0, len(inter)):
      calories[i] += inter[i]