class Solution:
    def divs(self, n):
        d = []
        for i in range(2, int(sqrt(n))+1):
            if n % i == 0:
                if len(d) > 0:
                    return [0]
                if i == n // i: # same number
                    continue
                d.append(i)
                d.append(n // i)
        return d
    def sumFourDivisors(self, nums: List[int]) -> int:
        ts = 0
        for n in nums:
            d = self.divs(n)
            #print(n ,d)
            if len(d) == 0:
                continue
            if d[0] == 0:
                continue
            else:
                ts += d[0] + d[1] + 1 + n
        return ts