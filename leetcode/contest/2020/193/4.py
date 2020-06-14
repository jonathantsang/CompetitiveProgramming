class TreeAncestor:

    def __init__(self, n, parent):
        self.pars = [parent]
        self.n = n
        for k in range(17):
            row = []
            for i in range(n):
                p = self.pars[-1][i]
                if p != -1:
                    p = self.pars[-1][p]
                row.append(p)
            self.pars.append(row)


    def getKthAncestor(self, node, k):
        """
        :type node: int
        :type k: int
        :rtype: int
        """
        i = 0
        while k:
            if node == -1: break
            if (k&1):
                node = self.pars[i][node]
            i += 1
            k >>= 1
        return node

# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
