class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        val = self.bettereven(n, 0)
        return val 
    
    def bettereven(self, n, steps):
        print(steps)
        if(n == 1):
            return steps
        ## If n is even, divide by 2 
        elif (n % 2 == 0):
            n = n / 2
            return self.bettereven(n, steps + 1)
        ## Else n is odd, check if the children of the even choices are 
        ## even, continuously to choose the better decision
        else:
            add1 = n + 1
            minus1 = n - 1
            newadd = add1 / 2
            newminus = minus1 / 2
            ## Decide what is n, based on which is even
            ## if newadd is even or it reaches one first, it is 
            ## picked otherwise, use minus1
            ## Check for newminus and newadd = 1 cases
            if(newminus == 1):
                n = newminus
                return self.bettereven(n, steps + 2) 
            if(newadd % 2 == 0 or newadd == 1):
                n = newadd
                return self.bettereven(n, steps + 2)
            else:
                n = newminus
                return self.bettereven(n, steps + 2)    