class Solution:
    def solve(self, s, t):
        # compare characters in strings
        def compare(w1, w2):
            amt = 0
            for c1,c2 in zip(w1, w2):
                if c1 != c2:
                    amt += 1
            return amt
        if s == "" and t == "":
            return 0

        ans = float('inf')
        # go through each index and compare the string to see minimal number of changes
        for i in range(len(s)-len(t)+1):
            ans = min(ans, compare(s[i:i+len(s)], t))

        return ans
