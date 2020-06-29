from collections import Counter

class Solution:
    def solve(self, s, t):
        chars = Counter(s)
        amt = 0
        for c in t:
            if c in chars and chars[c] >= 1:
                chars[c] -= 1
            else:
                amt += 1
        return amt
