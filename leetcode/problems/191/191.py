class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        one = 0
        num = ""
        while n > 0:
            if n % 2 == 1:
                num += "1"
            else:
                num += "0"
            n /= 2
        for d in str(num):
            #print(d)
            if d == "1":
                one += 1
        return one
        