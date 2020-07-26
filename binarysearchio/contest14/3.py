class Solution:
    def solve(self, nums, k):
        if k == 0:
            return []

        window = []
        for i,v in enumerate(nums):
            while window and window[-1] > v:
                # if we pop, still has enough in array to fill k
                if (len(window)+(len(nums)-i)-1) >= k:
                    window.pop()
                else:
                    break
            window.append(v)
        return list(window)[:k]
