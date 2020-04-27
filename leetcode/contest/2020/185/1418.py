class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        tables = defaultdict(dict) # num -> foods -> count
        foods = []
        nums = []
        for o in orders:
            if o[2] in tables[o[1]]:
                tables[o[1]][o[2]] += 1
            else:
                tables[o[1]][o[2]] = 1
            if o[2] not in foods:
                foods.append(o[2])
            if int(o[1]) not in nums:
                nums.append(int(o[1]))
        foods.sort()
        nums.sort()
        ans = []
        header = ["Table"]
        header.extend(foods)
        ans.append(header)
        for t in nums:
            row = [str(t)]
            for i in range(0, len(foods)):
                if foods[i] not in tables[str(t)]:
                    row.append("0")
                else:
                    row.append(str(tables[str(t)][foods[i]]))
            ans.append(row)
        return ans
            
