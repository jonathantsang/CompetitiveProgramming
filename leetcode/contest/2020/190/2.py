import collections

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v = set(['a', 'e', 'i', 'o', 'u'])
        window = collections.deque()
        ans = 0
        vowels = 0
        for c in s:
            if len(window) < k:
                window.append(c)
            else:
                a = window.popleft()
                if a in v:
                    vowels -= 1
                window.append(c)
            if c in v:
                vowels += 1
            ans = max(ans, vowels)
        return ans
            
