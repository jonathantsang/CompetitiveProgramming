class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True
        stack = []
        # (, ), e for 0, 1, 2
        left = 0
        right = 0
        stars = 0
        for i in range(0, len(s)):
            if s[i] == "(":
                left += 1
                stack.append("(")
            elif s[i] == ")":
                right += 1
                if len(stack) != 0 and stack[-1] == "(":
                    stack.pop()
                    right -= 1
                    left -= 1
                else:
                    print("star check on )")
                    # check stars possible
                    if stars + right < left:
                        return False
            elif s[i] == "*":
                stars += 1
            # print(left, right, stars)
            # print(stack, stars)
        return True
                