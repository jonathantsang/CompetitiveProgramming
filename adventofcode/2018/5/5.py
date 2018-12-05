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
while(len(word) != 11): # 11th is '/n'
  save = word
  word = shorten(word)
  print(len(word))
  if save == word:
    break
  
print(word)
print(len(word))
      
## 11
# dabCBAcaDA

# 11
# dabCBAcaDA