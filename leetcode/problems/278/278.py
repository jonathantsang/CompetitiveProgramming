# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def dnc(self, start, end):
        last = False
        ## Binary search style
        mid = (start + end) // 2
        check = isBadVersion(mid)
        if(start >= end):
            last = True
        if(check == True):
            ## Check if the one before is not bad
            if(mid > 1 and not isBadVersion(mid - 1)):
                return mid
            if(last == True):
                return 1
            return self.dnc(start, mid -1)
        else:
            if(last == True):
                return 1
            return self.dnc(mid + 1, end)
            
        
        
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        return self.dnc(start, end)