class RecentCounter(object):

    def __init__(self):
        self.vals = []
        self.start = 0
        
    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.vals.append(t)
        ## [t-3000, t]
        for i in range(self.start, len(self.vals)):
            if self.vals[i] >= t-3000:
                self.start = i
                break
        return len(self.vals) - self.start


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)