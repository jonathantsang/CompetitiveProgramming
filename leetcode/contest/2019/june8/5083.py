class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split()
        ans = []
        if len(words) <= 2:
            return ans
        for i, word in enumerate(words):
            if i >= len(words)-2:
                break # No second, out of bounds
            if word == first and words[i+1] == second:
                ans.append(words[i+2])
        return ans