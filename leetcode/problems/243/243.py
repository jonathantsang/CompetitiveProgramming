class Solution:
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        place = {} # key: word, value: index
        for i in range(0, len(words)):
            if words[i] in place:
                place[words[i]].append(i)
            else:
                place[words[i]] = [i]
        # look for word2 from word1
        dist = 9999999
        for i in place[word1]:
            for j in place[word2]:
                dist = min(dist, abs(i - j))
        return dist