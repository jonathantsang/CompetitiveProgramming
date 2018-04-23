class Solution(object):
    
    ## Returns the last index that was the same
    def compare(self, sub, fullString):
        mini = min(len(sub), len(fullString))
        for i in range(0, mini):
            if(sub[i] != fullString[i]):
                return i - 1
        return len(sub) - 1
    
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if(strs == []):
            return ""
        lcp = strs[0]
        for word in strs:
            if(lcp == ""):
                return ""
            longest = self.compare(lcp, word)
            lcp = word[:longest+1]
        return lcp
            
            