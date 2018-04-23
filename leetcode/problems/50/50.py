class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        else:
            answer = self.powPos(x, abs(n))
            if x < 0:
                #check if we need to add the negative
                if n % 2 != 0:
                    if answer > 0:
                        answer *= -1
            return answer if n > 0 else 1/answer
    '''
    Log(n) split
    '''
    def powPos(self, x, n):
        if abs(x - 0.0) <= sys.float_info.epsilon:
            #less than machine epsilon
            return x
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n % 2 == 0:
            #even power
            return self.powPos(x*x, n / 2)
        else:
            #odd power
            return x*self.powPos(x*x, n//2)