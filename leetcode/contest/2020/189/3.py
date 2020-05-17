class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        sets = {} # indice, set
        for i, p in enumerate(favoriteCompanies):
            sets[i] = set(p)

        ans = []
        for i in sets:
            subset = False
            for j in sets:
                if j == i:
                    continue
                if len(sets[i] - sets[j]) == 0:
                    subset = True
                    break
            if not subset:
                ans.append(i)

        return ans
                
