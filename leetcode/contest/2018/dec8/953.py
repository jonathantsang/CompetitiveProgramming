class Solution(object):
    def translate(self, word, letters):
        f = ""
        for c in word:
            f += letters[c]
        return f
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        letters = dict()
        for i in range(0, len(order)):
            letters[order[i]] = chr(97 + i)
        # print(letters)
        transformed = []
        for word in words:
            transformed.append(self.translate(word, letters))
        for i in range(0, len(transformed)-1):
            if transformed[i] > transformed[i+1]:
                return False
        return True
        
        
        