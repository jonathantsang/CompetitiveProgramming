class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        end = 1
        goesIn = 0
        if divisor == 0:
            return sys.maxint
        if((dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0)):
            end = -1
        divisor = abs(divisor)
        num = abs(dividend)
        sub = divisor
        c = 1
        while num >= divisor:
            if(num >= sub):
                num -= sub
                goesIn += c
                sub = sub << 1
                c = c << 1
            else:
                sub = sub>>1
                c = c>>1
        return min(max(-2147483648,end * goesIn),2147483647)