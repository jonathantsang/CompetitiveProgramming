import sys

n = int(sys.stdin.readline())
enc = dict()

j = 'a'
for i in range(2, 8):
  enc[j] = i
  enc[chr(ord(j)+1)] = i * 10 + i
  enc[chr(ord(j)+2)] = i * 100 + i * 10 + i
  j = chr(ord(j)+3)
  
j = 't'
for i in range(8, 10):
  enc[j] = i
  enc[chr(ord(j)+1)] = i * 10 + i
  enc[chr(ord(j)+2)] = i * 100 + i * 10 + i
  j = chr(ord(j)+3)

enc['s'] = 7777
enc['z'] = 9999
enc[' '] = 0

## print enc
for i in range(0, n):
  word = sys.stdin.readline().split('\n')[0]
  final = "Case #" + str(i+1) + ": "
  last = '-1'
  for char in word:
    if last == str(enc[char])[0]:
      final += " " + str(enc[char])
    else:
      final += str(enc[char])
    last = str(enc[char])[0]
  print final