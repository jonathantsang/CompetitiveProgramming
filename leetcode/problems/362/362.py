class HitCounter:
    # Plan
    # keep track of hits and timestamp
    # need -300 values for it to be valid
    # can just go through values and find what is valid, pop off what is not, give size of the queue

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        
        

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        self.stack.append(timestamp)
        

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        while len(self.stack) > 0 and timestamp - 300 >= self.stack[0]:
            self.stack.pop(0)
        return len(self.stack)
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)