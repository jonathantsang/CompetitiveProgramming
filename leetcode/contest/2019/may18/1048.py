class Solution:
    seen = {} # Key: word, Value: best path up to this prior
    # Get longest path from graph
    def run(self, word, graph, path):
        best = 0
        #print("at", word, path) 
        if word not in graph:
            self.seen[word] = 0
            return path
        if word in self.seen:
            return 0 # Already checked
        
        self.seen[word] = path
        
        for nextword in graph[word]:
            if nextword in self.seen:
                best = max(best, self.seen[nextword] + path)
            else:
                best = max(best, self.run(nextword, graph, path+1))
        
        return best
    
    # Check if word1 is a predecessor of word2
    def predecessor(self, word1, word2):
        if len(word1) + 1 != len(word2):
            return False
        
        # Edge case
        if len(word1) == 1 and len(word2) == 2:
            return (word1 == word2[0] or word1 == word2[1])
        
        onechar = False
        for i in range(0, len(word1)):
            if onechar:
                if word1[i] != word2[i+1]:
                    return False
                # Else same fine
            else:
                if word1[i] != word2[i]:
                    onechar = True
                    # Check one char ahead, for this one
                    if word1[i] != word2[i+1]:
                        return False
                # Else same fine
        return True
            
    def longestStrChain(self, words: List[str]) -> int:
        self.seen = {} # reset
        graph = {} # Key: word, Value: [words that it is a predecessor to]
        words.sort(key = len)
                
        # Word chain
        # predescessor add one letter anywhere in word1
        for i, word1 in enumerate(words):
            for j in range(i+1, len(words)):
                word2 = words[j]
                if len(word1)+1 < len(word2):
                    break
                res = self.predecessor(word1, word2)
                if res:
                    if word1 in graph:
                        graph[word1].append(word2)
                    else:
                        graph[word1] = [word2]
        #print(graph)
        
        # Try to get longest path from each word
        best = 0
        for word in words:
            if word in self.seen:
                continue
            best = max(best, self.run(word, graph, 1))
            
        # print(self.seen)
            
        return best