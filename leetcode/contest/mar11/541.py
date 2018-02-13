class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        start = 0
        end = start + 2 * k
        leng = len(s)
        while(True):
            if(start + 2 * k < leng):
                ## Reverse k digits
                ## update start and end
                rev = s[start:start + k]
                rev = rev[::-1]
                s = s[:start] + rev + s[start+k:]
                start = start + 2 * k
                end = start + 2 * k
            elif(start + 2 * k >= leng and start + k < leng):
                ## Reverse k digits, leave rest
                ## update start and end
                rev = s[start: start + k]
                rev = rev[::-1]
                s = s[:start] + rev + s[start+k:]
                return s
            else:
                ## since start + k > leng
                ## reverse the rest of the characters
                rev = s[start:]
                rev = rev[::-1]
                s = s[:start] + rev
                return s