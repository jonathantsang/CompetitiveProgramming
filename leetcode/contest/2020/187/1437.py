import collections

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        window = collections.deque()

        for i, v in enumerate(nums):
            #print(window)
            if v == 1:
                window.append(i)

            if len(window) > 0 and window[0] < i - k:
                window.popleft()

            if len(window) > 1:
                return False

        return True
