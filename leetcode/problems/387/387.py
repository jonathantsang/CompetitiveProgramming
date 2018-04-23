class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        ht = dict()
        min = 0
        for i in range(0, len(s)):
            if s[i] not in ht:
                ht[s[i]] = 1
            else:
                ht[s[i]] += 1
        for i in range(0, len(s)):
            if ht[s[i]] == 1:
                return i
        return -1