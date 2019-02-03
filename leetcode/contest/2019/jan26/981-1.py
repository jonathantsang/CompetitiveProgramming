class TimeMap:    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ht = {} # key: key of set, value: dict of: key: timestamp, value: value

    def set(self, key: 'str', value: 'str', timestamp: 'int') -> 'None':
        if key not in self.ht:
            self.ht[key] = { timestamp: value }
        else:
            self.ht[key][timestamp] = value
        

    def get(self, key: 'str', timestamp: 'int') -> 'str':
        if key not in self.ht:
            return ""
        else:
            # print("searching")
            previous = -1
            for ts, value in sorted(self.ht[key].items()):
                # print(ts, value)
                if ts > timestamp:
                    if previous == -1:
                        return ""
                    return self.ht[key][previous]
                previous = ts
            if previous == -1:
                return ""
            return self.ht[key][previous]
        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)