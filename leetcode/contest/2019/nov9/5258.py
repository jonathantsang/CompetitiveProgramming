import collections

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        dp = collections.Counter() # Key: tuple of chars sorted -> amt
        wordAmt = {} # Key: word -> amt in points
        wordSet = {} # Key: word -> ht of chars
        
        def makeHash(ht):
            v = ""
            for key in ht:
                v += str(key) + str(ht[key])
            return v
        
        def checkSets(s1, s2):
            for e in s1:
                if e not in s2 or s2[e] < s1[e]:
                    return False
            return True
        
        # s2 is full letters, s1 is word
        def subtractSet(s1, s2):
            newval = collections.Counter()
            for e in s2:
                newval[e] = s2[e]
                if s1[e] != 0 and s2[e] - s1[e] >= 0:
                    newval[e] -= s1[e]
            return newval
            
        def shrinkSet(lettersSet, score, skip):
            #print(lettersSet, "my score ", score, skip)
            v = makeHash(lettersSet)
            #print(v)
            if v in dp and score < dp[v]:
                return
            else:
                dp[v] = max(dp[v], score)
            for i, word in enumerate(words):
                if i in skip and skip[i] == 1:
                    continue
                if checkSets(wordSet[word], lettersSet) == False:
                    skip[i] = 1
                elif checkSets(wordSet[word], lettersSet) == True:
                    skip[i] = 1
                    # print("add ", word)
                    shrinkSet(subtractSet(wordSet[word], lettersSet), score + wordAmt[word], skip)
                    skip[i] = 0
            # print("cancel")
        
        scores = {} # Key: char -> amt
        for c in range(ord('a'), ord('z')+1):
            scores[chr(c)] = score[c-97]        

        for word in words:
            wordAmt[word] = 0
            wordSet[word] = collections.Counter()
            for c in word:
                wordAmt[word] += scores[c]
                wordSet[word][c] += 1
                
        lettersSet = collections.Counter() # Key: char -> count
        for c in letters:
            lettersSet[c] += 1
                
        # print(wordAmt)
        
        # top down enumeration
        skip = {}
        for i, word in enumerate(words):
            if checkSets(wordSet[word], lettersSet) == False:
                # Entirely skip since word cannot be created
                skip[i] = 1
            else:
                shrunkSet = subtractSet(wordSet[word], lettersSet)
                v = makeHash(lettersSet)
                dp[v] = max(wordAmt[word], dp[v])
                # print(shrunkSet, " start ", word)
                skip[i] = 1
                shrinkSet(shrunkSet, wordAmt[word], skip)
                skip[i] = 0
        
        if len(dp) == 0:
            return 0
        return max(dp.values())
                