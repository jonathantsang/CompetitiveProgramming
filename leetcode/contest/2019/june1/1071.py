class Solution:
    def divides(self, str1, str2):
        ans = str1
        while(len(ans) < len(str2)):
            ans += str1
        return ans == str2
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        best = ""
        for i in range(1, min(len(str1), len(str2))+1):
            pieces = str1[:i]
            # print(pieces)
            if self.divides(pieces, str1) and self.divides(pieces, str2):
                best = pieces
        return best