class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        total = num
        while len(str(total)) != 1:
            total = 0
            for d in str(num):
                total += int(d)
            num = total
            # print(total)
        return total