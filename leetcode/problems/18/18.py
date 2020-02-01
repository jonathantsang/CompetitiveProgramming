class Solution:
    soln = {}
    def twoSum(self, nums, pairs, target):
        ht = {}
        for pair in pairs:
            if target - pair[0] in ht:
                # check duplicates
                for p in ht[target - pair[0]]:
                    s = set()
                    for a in [p[2], p[1], pair[1], pair[2]]:
                        s.add(a)
                    if len(s) == 4:
                        #print(s)
                        a = []
                        for v in s:
                            a.append(nums[v])
                        a.sort()
                        #print(a)
                        self.soln[(a[0], a[1], a[2], a[3])] = 1
            if pair[0] in ht:
                ht[pair[0]].append(pair)
            else:
                ht[pair[0]] = [pair]
            
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.soln = {}
        pairs = []
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                val = nums[i] + nums[j]
                pairs.append((val,i,j))
        pairs.sort()
        # print(pairs)
        self.twoSum(nums, pairs, target)
        a = []
        for p in self.soln:
            a.append(p)
        a.sort()
        return a