from collections import deque, defaultdict

class Solution:
    def solve(self, tree, color):
        # tree: [parent, children] for ith node ([0] has no parent)
        # color: for ith node

        self.special = 0

        # pass up set of values
        def dfs(node, par): # node is node #, par is parent
            s = set([color[node]])
            for child in tree[node]:
                if child != par:
                    a = dfs(child, node)
                    if a != None and s != None:
                        ls = len(s)
                        la = len(a)
                        if ls <= la:
                            a |= s
                            s = a
                        else:
                            s |= a
                        if len(s) != la + ls:
                            s = None
                    else:
                        s = None

            if s != None:
                self.special += 1

            return s

        dfs(0, -1)
        return self.special
