class Solution:
    def findIntegers(self, num):
        """
        :type num: int
        :rtype: int
        """
        total = num
        saved = num
        if(num == 1):
            return 2
        if(num == 2):
            return 3
        if(num == 3):
            return 3
        maxi = 0
        num = num // 3
        if (num < 1):
            maxi = 0
        elif (num == 0):
            maxi = 0
        else:
            maxi = 1
        while(num > 2):
            num = num // 2
            maxi += 1
        if(num == 0):
            maxi -= 1
        else:
            total += 1
        # maxi is the number of zeroes
        counter = maxi
        total += saved
        for z in range(0, maxi):
            total -= ((2**counter) - 1)
            counter -= 1
        return total