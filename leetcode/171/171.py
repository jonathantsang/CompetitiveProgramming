class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        leng = len(s)
        sum = ord(s[0])-64
        for i in range(1, leng):
            print(sum)
            sum = sum * 26 + (ord(s[i]) - 64)
            print(sum)
        return sum