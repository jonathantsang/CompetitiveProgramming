class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        divisor = 2
        limit = math.sqrt(num)
        sumOfDivisors = 1
        while(divisor <= limit):
            if(num % divisor == 0):
                compliment = num / divisor
                ## Add compliment as long as it is not the number itself
                if(compliment != num):
                    sumOfDivisors += compliment
                sumOfDivisors += divisor
            divisor += 1
        print sumOfDivisors
        return sumOfDivisors == num