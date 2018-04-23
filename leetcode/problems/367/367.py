class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        counter = 1
        odd = 1
        while(counter <= num):
            if(counter == num):
                return True
            odd += 2
            counter += odd
            print(counter)
        return False