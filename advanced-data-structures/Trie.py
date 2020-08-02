class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_node = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        root = self.root
        for symbol in word:
            dic_to_search = root.children
            if symbol not in dic_to_search:
                dic_to_search[symbol] = TrieNode()
            root.children = dic_to_search
            root = root.children[symbol]
        root.end_node = 1

    def search(self, word):
        node = self.root
        idx = 0
        while node:
            if idx == len(word) and node.end_node:
                return True
            if word[idx] not in node.children:
                return False
            node = node.children[word[idx]]
        return False
