class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for w in words:
            for w2 in words:
                if w in w2 and w != w2 and w not in ans:
                    ans.append(w)
        return ans
