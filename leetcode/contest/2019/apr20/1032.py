class StreamChecker:
    def addToTrie(self, trie, word):
        #word = word[::-1]
        ref = trie
        for i, c in enumerate(word):
            # Keep a reference deeper in trie
            if c in ref:
                ref = ref[c]
            else:
                ref[c] = {} # new dict
                ref = ref[c]
            # Last one
            if i == len(word)-1:
                ref[-1] = 1 # Meaning it is valid word
    
    def __init__(self, words: List[str]):
        self.trie = {} # Key: character, Value: dictionary of 26 possible values denotes more characters
        # The key having a -1 value in the dict means it is a word
        self.active = [] # Active trie nodes, so it can be updated when a new query arrives
        for word in words:
            self.addToTrie(self.trie, word)
            
        # print(self.trie)
        

    def query(self, letter: str) -> bool:
        finished = False
        
        # Check active
        reactive = []
        for i, node in enumerate(self.active):
            if letter in node:
                reactive.append(node[letter])
                # Check if finished
                if -1 in node[letter]:
                    finished = True
        
        # Check root?
        if letter in self.trie:
            # Check if finished
            if -1 in self.trie[letter]:
                finished = True
            else:
                # Add it
                reactive.append(self.trie[letter])
        
        self.active = reactive # Swap over
        return finished
                    
# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)