class Solution:
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        window = list()
        maxLen = 0
        seen = dict() ## stores last seen
        i = 0
        for type in tree:
            ## print(window)
            if type in seen:
                window.append(type)
                seen[type] = len(window)-1
            elif len(seen) < 2:
                window.append(type)
                seen[type] = len(window)-1
            else:
                ## Need to pop until seen from whichever one last seen is earlier
                earlier = 9999999
                destroy = window[0]
                for key in seen:
                    if(seen[key] < earlier):
                        earlier = seen[key]
                        destroy = key
                        
                firstElement = destroy
                popIdx = earlier
                ## print(popIdx)
                for j in range(0, popIdx+1):
                    window.pop(0)
                del seen[firstElement]
                ## Update other key as well based on popping
                for key in seen:
                    seen[key] -= (popIdx+1)
                
                ## Add the element from type
                window.append(type)
                seen[type] = len(window)-1
                
            maxLen = max(maxLen, len(window))
            i+=1
        return maxLen