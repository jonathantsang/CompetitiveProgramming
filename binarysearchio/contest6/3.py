import collections

class Solution:
    def solve(self, requests, u, g):
        # Write your code here
        last = collections.defaultdict(collections.deque) # user, window deque
        total = collections.deque()
        
        windowtime = 60
        requests.sort(key=lambda x: [x[1], x[0]])
        
        amt = 0
        for r in requests:
            uid, time = r
            
            while len(total) > 0 and total[0] + windowtime <= time:
                total.popleft()
            
            while len(last[uid]) > 0 and last[uid][0] + windowtime <= time:
                last[uid].popleft()
                
            # space?
            if len(total) < g and len(last[uid]) < u:
                last[uid].append(time)
                total.append(time)
                amt += 1
        return amt