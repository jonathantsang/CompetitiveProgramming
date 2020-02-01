import collections
import re

with open('i') as f:
  lines = [l.rstrip('\n') for l in f]

  alllet = set()
  deps = collections.defaultdict(set)
  for line in lines:
    m = re.match(r'^Step (.) must be finished before step (.) can begin.$', line)
    deps[m.group(2)].add(m.group(1))
    alllet.add(m.group(2))
    alllet.add(m.group(1))

  reml = sorted(alllet)
  done = set()
  order = ''
  while reml:
    for i, c in enumerate(reml):
      if not (deps[c] - done):
        order += c
        done.add(c)
        del reml[i]
        break
  print order
    
  reml = sorted(alllet)
  done_time = {}
  busy_until = [0, 0, 0, 0, 0]
  order = ''
  time = 0
  while reml:
    if all(t > time for t in busy_until):
      time = min(busy_until)
    for i, c in enumerate(reml):
      if all(d in done_time and done_time[d] <= time for d in deps[c]):
        order += c
        for ib, b in enumerate(busy_until):
          if b <= time:
            busy_until[ib] = time + 60 + ord(c) - 64
            done_time[c] = busy_until[ib]
            break
        print c, 'starts at', time, 'done at', done_time[c]
        del reml[i]
        break
    else:
      time = min(t for t in busy_until if t > time)
  
  print max(busy_until)
  
# BGKDMJCNEQRSTUZWHYLPAFIVXO soln
# BGKDMJCNEQRSTUZWHYLPAFIVXO # mine
# BQRGKDMJCNESTUZWHYLPAFIVXO # old