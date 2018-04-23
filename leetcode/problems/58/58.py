class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        strs = s.split(" ")
        numo = 0
        print(strs)
        for i in range(len(strs)-1, -1, -1):
            if(strs[i] != ''):
                numo = i
                break;
        return len(strs[numo])