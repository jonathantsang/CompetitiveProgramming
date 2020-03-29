import collections
class Solution:
    def longestPrefix(self, s: str) -> str:
        for i in range(len(s)-1, 0, -1):
            pre = s[:i]
            suf = s[len(s) - i:]
            #print(pre, suf)
            if pre == suf:
                return pre
        return ""
            