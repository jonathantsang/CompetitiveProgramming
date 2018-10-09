import sys

lookup = dict()
lookup['a'] = '@'
lookup['b'] = '8'
lookup['c'] = '('
lookup['d'] = '|)'
lookup['e'] = '3'
lookup['f'] = '#'
lookup['g'] = '6'
lookup['h'] = '[-]'
lookup['i'] = '|'
lookup['j'] = '_|'
lookup['k'] = '|<'
lookup['l'] = '1'
lookup['m'] = '[]\/[]'
lookup['n'] = '[]\[]'
lookup['o'] = '0'
lookup['p'] = '|D'
lookup['q'] = '(,)'
lookup['r'] = '|Z'
lookup['s'] = '$'
lookup['t'] = "']['"
lookup['u'] = '|_|'
lookup['v'] = '\/'
lookup['w'] = '\/\/'
lookup['x'] = '}{'
lookup['y'] = '`/'
lookup['z'] = '2'


line = sys.stdin.readline()
final = ""
for char in line:
  if char.lower() in lookup:
    final += lookup[char.lower()]
  else:
    final += char
print final