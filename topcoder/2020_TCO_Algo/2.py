def sum_digits(n):
	s = 0
	while n:
		n, remainder = divmod(n, 10)
		s += remainder
	return s

class EllysWhatDidYouGet:
	def getCount(self, N):
		ans = 0
		for x in range(1, 51):
			for y in range(1, 51):
				for z in range(1, 51):
					same = -1
					valid = True
					for n in range(1, N+1):
						val = (n * x + y) * z
						if n == 1:
							same = sum_digits(val)
							continue
						elif same != sum_digits(val):
							valid = False
							break
					if valid:
						ans += 1
		return ans