class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.number_of_groups = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_parent, y_parent = self.find(x), self.find(y)
        if x_parent == y_parent:
            return False
        if self.rank[x_parent] < self.rank[y_parent]:
            x_parent, y_parent = y_parent, x_parent

        if self.rank[x_parent] == self.rank[y_parent]:
            self.rank[x_parent] += 1

        self.parent[y_parent] = x_parent

        self.number_of_groups -= 1
        return True
