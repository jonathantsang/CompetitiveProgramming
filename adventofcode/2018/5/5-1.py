import math
import sys

seen = dict()

def shorten(word):
  i = 97 # lower-case
  j = 65 # caps
  while(i < 123):
    forward = chr(i) + chr(j)
    backward = chr(j) + chr(i)
    word = word.replace(forward, '')
    word = word.replace(backward, '')
    i += 1
    j += 1
  return word

word = sys.stdin.readline()
total = word

smallestLeng = 9999999
for i in range(0, 26):
  low = chr(i + 97)
  cap = chr(i + 65)

  word = total.replace(low, '').replace(cap, '')
  save = ''
  
  while(True): # 11th is '/n'
    save = word
    word = shorten(word)
    if save == word:
      break
  smallestLeng = min(smallestLeng, len(word))
  
  print(smallestLeng)