class Solution:
    def h(self, string):
        arr = [0 for i in range(0, 26)]
        for c in string:
            arr[ord(c)-97] += 1
        return tuple(arr)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {} # Key: hashcode, Value: strings
        for word in strs:
            a = self.h(word)
            # print(a, word)
            if a in groups:
                groups[a].append(word)
            else:
                groups[a] = [word]

        ans = []
        for ht in groups:
            ans.append(groups[ht])
        return ans