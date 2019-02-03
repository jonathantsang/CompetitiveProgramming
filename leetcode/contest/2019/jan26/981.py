class Node: # Used for BST
    def __init__(self, timestamp, value):
        self.timestamp = timestamp
        self.value = value
        self.left = None
        self.right = None

class TimeMap:
    def addValue(self, node, timestamp, value):
        if node:
            if timestamp > node.timestamp:
                if node.right != None:
                    self.addValue(node.right, timestamp, value)
                else:
                    node.right = Node(timestamp, value)
            else:
                if node.left != None:
                    self.addValue(node.left, timestamp, value)
                else:
                    node.left = Node(timestamp, value)
    
    def findValue(self, node, timestamp):
        # print("finding, at ", node.timestamp, " for ", timestamp)
        if node:
            if node.timestamp == timestamp:
                # print("found for ", node.value)
                return node.value
            if node.timestamp > timestamp: # too big, go left
                if node.left == None:
                    return ""
                else:
                    return self.findValue(node.left, timestamp)
            elif node.timestamp < timestamp: # works, but could be too small, go right
                if node.right == None:
                    return node.value # can't go further
                else:
                    a = self.findValue(node.right, timestamp)
                    if a == "": # aka lower level couldn't resolve
                        return node.value # my value works, but may not be optimal
                    else:
                        return a
        return ""
        
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ht = {} # key: key of set, value: BST of Node with value of timestamp, and data

    def set(self, key: 'str', value: 'str', timestamp: 'int') -> 'None':
        if key not in self.ht:
            self.ht[key] = Node(timestamp, value)
        else:
            self.addValue(self.ht[key], timestamp, value)
        

    def get(self, key: 'str', timestamp: 'int') -> 'str':
        if key not in self.ht:
            return ""
        else:
            # print("searching")
            return self.findValue(self.ht[key], timestamp)
        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)