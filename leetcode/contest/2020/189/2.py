class Solution:
    def arrangeWords(self, text: str) -> str:
        text = text.split(' ')
        text[0] = text[0][0].lower() + text[0][1:]
        words = []
        for i, w in enumerate(text):
            words.append((len(w), i, w))
        words.sort()
        ans = []
        for w in words:
            ans.append(w[2])
        ans[0] = ans[0][0].upper() + ans[0][1:]
        return " ".join(ans)
