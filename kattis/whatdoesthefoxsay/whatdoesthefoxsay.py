#! /usr/bin/python3

import sys
import math

n = sys.stdin.readline()

for i in range(0, int(n)):
  
  words = list(sys.stdin.readline().split())
  # print(words)
  line = ""
  
  while True:
    line = sys.stdin.readline()
    if line == "what does the fox say?\n":
      break
    
    # print("line", line)
    sound = line.split('goes ')[1].split('\n')[0]
    # print("sound", sound)
    words = list(filter(lambda a: a != sound, words))
    
  ans = ""  
  for word in words:
    ans += word + " "
  if ans[len(ans)-1] == "":
    ans = ans[:len(ans)-1]
  print(ans)