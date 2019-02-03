# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    seen = {} # key: node id, value: [x, y]
    smallest = 99999999
    biggest = 0
    def traverse(self, node, x, y):
        if node:
            # print(node.val, score)
            # print(node.val)
            self.seen[node.val] = [x, y]
            self.smallest = min(self.smallest, x)
            self.biggest = max(self.biggest, x)
            self.traverse(node.left, x-1, y-1)
            self.traverse(node.right, x+1, y-1)
                
    def verticalTraversal(self, root: 'TreeNode') -> 'List[List[int]]':
        self.seen = {} # key: node id, value: level
        self.smallest = 99999999
        self.biggest = 0
        
        self.traverse(root, 0, 0)
        ans = [[] for x in range(0, self.biggest - self.smallest + 1)]
                
        #print(ans)
        #print(self.smallest)
        #print(self.biggest)
        for s in self.seen:
            ans[self.seen[s][0] - self.smallest].append([-self.seen[s][1], s])
        
        #print(self.seen)
        #print(ans)
            
        for i in range(0, len(ans)):
            row = ans[i]
            row.sort()
            for i in range(0, len(row)):
                row[i] = row[i][1]
        
        # sort each row
        return ans
        