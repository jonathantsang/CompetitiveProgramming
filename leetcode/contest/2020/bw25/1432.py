class Solution:
    def maxDiff(self, num: int) -> int:
        number = str(num)

        # first non 1 and non 9 digit
        zero = '-1'
        one = '-1'
        nine = '-1'
        for i, d in enumerate(number):
            if d != '0' and zero == '-1' and i != 0 and d != number[0]:
                zero = d
            if d != '1' and one == '-1':
                one = d
            if d != '9' and nine == '-1':
                nine = d

        #print(nine, one, zero)

        # largest
        x = nine
        y = '9'
        a = number.replace(x, y)

        b = number

        if zero != -1:
            # smallest
            x = zero
            y = '0'
            b = number.replace(x, y)

        # one
        x = one
        y = '1'
        b = min(int(b), int(number.replace(x, y)))

        #print(a, b)

        return abs(int(a) - int(b))
        
