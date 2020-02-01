def maxScoreWords(self, words, letters, SCORE):
        def cvt(word):
            ans = [0] * 26
            for letter in word:
                i = ord(letter) - ord('a')
                ans[i] += 1
            return ans
        
        def score(count):
            ans = 0
            for i, c in enumerate(count):
                ans += c * SCORE[i]
            return ans

        words = map(cvt, words)
        letters = cvt(letters)
        wordscores = map(score, words)
        ans = 0
        N = len(words)
        for sz in xrange(N + 1):
            for cand in itertools.combinations(xrange(N), sz):
                bns = sum(wordscores[i] for i in cand)
                if bns <= ans: continue
                # is it possible
                count = letters[:]
                for i in cand:
                    for j, c in enumerate(words[i]):
                        count[j] -= c
                if all(c >= 0 for c in count):
                    ans = bns
        return ans