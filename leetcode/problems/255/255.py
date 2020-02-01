class Solution:
    def verify(self, preorder, i, minval, maxval):
        if i >= len(preorder) or preorder[i] > maxval:
            return True
        if preorder[i] >= minval and preorder[i] <= maxval:
            a = self.verify(preorder, i*2+1, minval, preorder[i])
            if a == False:
                return False
            b = self.verify(preorder, i*2+2, preorder[i], maxval)
            if b == False:
                return False
            return True
        return False
        
    def verifyPreorder(self, preorder: List[int]) -> bool:
        if preorder == []:
            return True
        return self.verify(preorder, 0, -float('inf'), float('inf'))