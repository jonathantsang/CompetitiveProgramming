class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True
        dp = [[0 for i in range(0, len(s))] for j in range(0, 3)]
        # (, ), e for 0, 1, 2
        left = 0
        right = 0
        stars = 0
        for i in range(0, len(s)):
            if s[i] == "(":
                left += 1
            elif s[i] == ")":
                right += 1
            elif s[i] == "*":
                stars += 1
                
            if left > right:
                dp[1][i] = left - right
                dp[2][i] = stars - (left - right)
            else:
                dp[0][i] = right - left
                dp[2][i] = stars - (right - left)
            print(dp)
            
            # Fail case too many )
            if (dp[0][i] > 0 and dp[2][i] < 0):
                return False
        
        for i in range(0, len(dp)):
            if dp[i][-1] < 0:
                return False
        return True
                