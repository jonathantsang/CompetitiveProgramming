class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ht = dict()
        for stri in s:
            if stri in ht:
                ht[stri] += 1
            else:
                ht[stri] = 1
        for stri in t:
            if stri in ht:
                ht[stri] -= 1
                if(ht[stri] < 0):
                    return stri
            else:
                return stri