import sys

case = int(sys.stdin.readline())

taxes = {} # Key: Item -> Value: [PST, GST, HST]

def round_half_up(n, decimals=2):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier + 0.5) / multiplier

for i in range(1, case+1):
  nm = list(sys.stdin.readline().split())
  n = int(nm[0])
  m = int(nm[1])
  for j in range(0, n):
  	name = list(sys.stdin.readline().split())
  	taxes[name] = [name[1][:-1], name[2][:-1], name[3][:-1]]

  difference = 0
  for j in range(0, m):
  	name = list(sys.stdin.readline().split())
  	percents = taxes[name]
  	hst = percents[2]
  	gstandpst = percents[0] + percents[1]
  	amount = name[1][1:]
  	hstpaid = amount * hst
  	gstpstpaid = amount * gstandpst
  	# Round at half a cent or more
  	hstpaid = round_half_up(hstpaid)
  	gstpstpaid = round_half_up(gstpstpaid)

  	difference += (hstpaid - gstpstpaid)

  print(difference)

