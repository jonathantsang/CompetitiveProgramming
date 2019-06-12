class Solution:
    seen = {} # Key: tuple, Value: 1
    def permutation(self, cur, nums, pos, sets, start):
        if cur != []:
            a = cur.copy()
            a.sort()
            b = tuple(a)
            if b not in self.seen:
                sets.append(cur.copy())
                self.seen[b] = 1
        
        if pos == len(nums):
            return
        
        # Don't Include
        self.permutation(cur, nums, pos+1, sets, start)
        
        # Include
        cur.append(nums[pos])
        self.permutation(cur, nums, pos+1, sets, start)
        cur.pop(len(cur)-1)
        
                         
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sets = [[]]
        for i in range(0, len(nums)):
            self.permutation([], nums, i, sets, i)
        return sets