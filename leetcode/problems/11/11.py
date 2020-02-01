class Solution:
    def maxArea(self, height: List[int]) -> int:
        import collections
        
        window = collections.deque()
        
        window.append(height[0])
        
        best = 0 
        
        for i in range(1, len(height)):
            if height[i] > window[0]:
                window.append(height[i])
                best = max(best, (len(window)-1) * window[0])
                while len(window) > 0 and height[i] > window[0]:
                    window.popleft()
            else:
                window.append(height[i])
                best = max(best, (len(window)-1) * height[i])
            
            #print(window, best)
            
        return best