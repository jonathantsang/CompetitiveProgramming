class Solution:
    def numSplits(self, s: str) -> int:
        N = len(s)
        s1 = Counter()
        s2 = Counter(s)
        ans = 0
        for i in range(N):
            #print(s1,s2)
            s1[s[i]]+=1
            s2[s[i]]-=1
            if s2[s[i]] == 0:
                del s2[s[i]]

            if len(s1) == len(s2):
                ans += 1

        return ans
