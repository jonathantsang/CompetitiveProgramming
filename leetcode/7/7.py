class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = 1
        if(x < 0):
            neg = -1
            x *= -1
        if(x > 2147483647 or x < -2147483648):
            return 0
        x = str(x)
        x = x[::-1]
        x = int(x) * neg
        if(x > 2147483647 or x < -2147483648):
            return 0
        return x