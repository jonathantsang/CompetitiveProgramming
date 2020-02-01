class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:        
        ans = []
        app = []
        ht = {} # Key: element, Value: Count
        for e in arr2:
            ht[e] = 0
                
        for e in arr1:
            if e in ht:
                ht[e] += 1
            else:
                app.append(e)
        app.sort()
        for e in arr2:
            for _ in range(0, ht[e]):
                ans.append(e)
        ans.extend(app)
        return ans