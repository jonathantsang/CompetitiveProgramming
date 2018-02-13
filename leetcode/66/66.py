class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        leng = len(digits)
        digits[leng-1] += 1
        if(digits[leng-1] > 9):
            for i in range(leng-1, -1, -1):
                if(i == 0 and digits[i] > 9):
                    digits.append(0)
                    digits[i] = 1
                    return digits
                if(digits[i] > 9):
                    digits[i] = 0
                    digits[i - 1] += 1
                else:
                    break
        return digits