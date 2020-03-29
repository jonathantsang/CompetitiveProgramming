class Solution:
    def incrementWord(self, word, idx):
        word = list(word)
        word[idx] = chr(ord(word[idx])+1)
        #print(idx)
        #print(word)
        for i in range(idx, -1, -1):
            if word[i] == '{':
                word[i] = 'a'
                if i == 0:
                    break
                else:
                    word[i-1] = chr(ord(word[i-1])+1)
            else:
                break
        #print(word)
        return "".join(word)
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        modulo = 10**9 + 7
        count = 0
        if s1 > s2:
            return 0
        saved = s1
        
        seen = {} # index seen at
        
        while saved <= s2:
            search = saved.find(evil)
            if search == -1 and len(saved) == n:
                # print(saved)
                count += 1
                saved = self.incrementWord(saved, len(saved)-1)
                if len(saved) != n:
                    break
            else:
                # need to move search + len(evil) -1 index
                saved = self.incrementWord(saved, search + len(evil) - 1)
        return count % modulo