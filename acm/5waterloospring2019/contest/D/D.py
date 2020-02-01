import sys
import math

case = int(sys.stdin.readline())

def round_half_up(n, decimals=2):
		multiplier = 10 ** decimals
		return math.floor(n * multiplier + 0.5) / multiplier

for i in range(1, case+1):
	taxes = {} # Key: Item -> Value: [PST, GST, HST]
	
	nm = list(sys.stdin.readline().split())
	n = int(nm[0])
	m = int(nm[1])
	for j in range(0, n):
		name = list(sys.stdin.readline().split())
		taxes[name[0]] = [name[1][:-1], name[2][:-1], name[3][:-1]]

	difference = 0
	for j in range(0, m):

		name = list(sys.stdin.readline().split())
		percents = taxes[name[0]]

		hst = float(percents[2])
		gst = float(percents[1])
		pst = float(percents[0])
		amount = float(name[1][1:])

		#print("percents")
		#print(hst, gst, pst, amount)

		hstpaid = amount * hst / 100.00
		gstpaid = amount * gst / 100.00
		pstpaid = amount * pst / 100.00

		#print("paid amt")
		#print(hstpaid, gstpaid, pstpaid)

		# Round at half a cent or more
		hstpaid = round_half_up(hstpaid)
		gstpaid = round_half_up(gstpaid)
		pstpaid = round_half_up(pstpaid)

		difference += (hstpaid - gstpaid - pstpaid)

	print(format(difference, '.2f'))

