class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = {}
        

    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        for w in dict:
            self.words[w] = 1
        

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        for w in self.words:
            if len(w) == len(word):
                if w == word:
                    continue
                # Check if replaceable
                for i, l in enumerate(w):
                    for c in range(ord('a'), ord('z') + 1):
                        formed = (w[:i] + chr(c) + w[i+1:])
                        # print(formed)
                        if formed == word:
                            return True
        return False
# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)