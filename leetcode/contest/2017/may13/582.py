class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        ## Stack to figure out what to kill
        stack = []
        killed = []
        stack.append(kill)
        
        ## make a ht with collisions
        storage = dict()
        for j in range(0, len(ppid)):
            ## Parent key gives children
            if ppid[j] not in storage:
                storage[ppid[j]] = [pid[j]]
            else:
                storage[ppid[j]].append(pid[j])
        print(storage)
        
        while(stack != []):
            ## Pop off the stack to check if the element is a parent
            newelem = stack.pop()
            ## Check for other new killed elements in ht, if it has children it will be in storage
            if newelem in storage:
                for elem in storage[newelem]:
                    stack.append(elem)
            killed.append(newelem)
        
        return killed
        
        