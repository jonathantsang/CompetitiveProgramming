class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for bracket in s:
            if bracket in dict.values():
                stack.append(bracket)
            elif bracket in dict.keys():
                if stack == [] or dict[bracket] != stack.pop():
                    return False
            else:
                return False
        return stack == []