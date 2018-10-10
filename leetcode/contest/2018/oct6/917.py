class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        chars = []
        for c in S:
            if c.isalpha():
                chars.append(c)
        chars = chars[::-1]
        i = 0
        final = ""
        for c in range(0, len(S)):
            if S[c].isalpha():
                final += chars[i]
                i+=1
            else:
                final += S[c]
        return final