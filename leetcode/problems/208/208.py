class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {} # Key: char, Value: Dict with more dicts for char. -1 in dict means also ends there
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        t = self.trie
        for c in word:
            if c not in t:
                t[c] = {}
                t = t[c]
            else:
                t = t[c]
        t[-1] = -1 # ending
                
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        t = self.trie
        for c in word:
            if c in t:
                t = t[c]
            else:
                return False
        return -1 in t
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        t = self.trie
        for c in prefix:
            if c in t:
                t = t[c]
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)