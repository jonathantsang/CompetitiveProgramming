class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n
        lst = []
        i = 1
        ## Find the max perfect square
        while i * i <= n:
            lst.append(i*i)
            i += 1
        cnt = 0
        ## Set of possible ps
        toCheck = {n}
        ## While the set is valid
        while toCheck:
            cnt += 1
            temp = set()
            ## For each level in BST
            for x in toCheck:
                ## Go to each element of the lst
                for y in lst:
                    ## Equal return cnt
                    if x == y:
                        return cnt
                    ## Else break
                    if x-y < 0:
                        break
                temp.add(x-y)
            toCheck = temp
        return cnt
        