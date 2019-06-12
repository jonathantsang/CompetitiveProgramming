# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    index = 1
    def construct(self, parent, current, preorder):
        # print(current.val)
        if self.index == len(preorder):
            return
        # Construct to the left
        if preorder[self.index] < current.val:
            current.left = TreeNode(preorder[self.index])
            self.index += 1
            if self.index == len(preorder):
                return
            self.construct(current, current.left, preorder)        
        else:
            # Greater than the value, but need to go up to find the node where it is greater than current, but less than parent
            if (parent.val > current.val and preorder[self.index] > current.val and preorder[self.index] < parent.val) or\
                (parent.val < current.val and preorder[self.index] > current.val and preorder[self.index] > parent.val):
                current.right = TreeNode(preorder[self.index])
                self.index += 1
                if self.index == len(preorder):
                    return
                
                # Make smart movement
                if (parent.val > current.val and preorder[self.index] < parent.val) or\
                    (parent.val < current.val and preorder[self.index] > current.val):
                    checkright = self.construct(current, current.right, preorder)
                else:
                    return # go up to parent to make better decision
            else:
                return
            
        if self.index == len(preorder):
            return
        # print("back at ", current.val, "index of ", self.index)
                
        # Afterwards, check if self.index is MY right
        if (parent.val > current.val and preorder[self.index] > current.val and preorder[self.index] < parent.val) or\
            (parent.val < current.val and preorder[self.index] > current.val and preorder[self.index] > parent.val):
            current.right = TreeNode(preorder[self.index])
            self.index += 1
            if self.index == len(preorder):
                return
            # Make smart movement
            # print("after right is", preorder[self.index])
            if (parent.val > current.val and preorder[self.index] < parent.val) or\
                (parent.val < current.val and preorder[self.index] > current.val):
                checkright = self.construct(current, current.right, preorder)
            else:
                return # go up to parent to make better decision
            
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        self.index = 1
        root = TreeNode(preorder[0])
        self.construct(TreeNode(float('inf')), root, preorder)
        return root