class Solution:
    def solve(self, k):
        # Write your code here
        fives = 0
        num = 5
        while num <= k:
            num *= 5
            fives += 1

        return fives
