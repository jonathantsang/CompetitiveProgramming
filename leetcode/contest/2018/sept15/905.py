class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even = list()
        odd = list()
        for a in A:
            if a % 2 == 0:
                even.append(a)
            else:
                odd.append(a)
        even.extend(odd)
        return even