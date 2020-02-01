"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        self.seen = {} # Key: reference to old node, Value: reference to new node
        
        newnode = Node(node.val, [])
        
        def traverse(oldnode, newnode):
            for nei in oldnode.neighbors:
                if nei in self.seen:
                    newnode.neighbors.append(self.seen[nei])
                else:
                    madenode = Node(nei.val, [])
                    self.seen[nei] = madenode
                    newnode.neighbors.append(self.seen[nei])
                    traverse(nei, madenode)            
            
        self.seen[node] = newnode
        traverse(node, newnode)
        
        return newnode