from collections import deque

class Solution:
    def solve(self, nums):
        prefix = deque([-float('inf')]) # max so far: 0 to i
        suffix = deque([float('inf')]) # min so far: N-1 to i
        N = len(nums)

        for i in range(N):
            prefix.append(max(prefix[-1], nums[i]))

        for j in range(N-1,-1,-1):
            suffix.appendleft(min(suffix[0], nums[j]))

        for k in range(1,len(prefix)-1):
            if prefix[k] < suffix[k]:
                return True
        return False

            
