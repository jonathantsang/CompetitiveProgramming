class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        if len(arr1) < len(arr2):
            arr1, arr2 = arr2, arr1
        i1 = len(arr1)-1
        i2 = len(arr2)-1
        carry = 0
        while(i1 >= 0 and i2 >= 0):
            # print(arr1[i1], arr2[i2])
            val = (arr1[i1] + arr2[i2]) + carry
            if val >= 2:
                carry = 1
                val %= 2
            ans.append(val)
            i1 -= 1
            i2 -= 1
        ans = ans[::-1]
        
        if i1 >= 0:
            ans = arr1[:i1+1] + ans
            ans[i1+1] += carry
            # print(ans)
            i1 = i1+1
            while(ans[i1] == 2):
                ans[i1] = 0
                i1 -= 1
                if i1 == -1:
                    ans.insert(0, 1)
                    break
                ans[i1] += 1
        return ans