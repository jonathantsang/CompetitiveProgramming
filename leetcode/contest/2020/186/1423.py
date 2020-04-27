class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        front = [0 for _ in range(len(cardPoints))]
        back = [0 for _ in range(len(cardPoints))]
        front[0] = cardPoints[0]
        back[-1] = cardPoints[-1]
        best = 0

        for i in range(1, k):
            front[i] = front[i-1] + cardPoints[i]
        for i in range(len(cardPoints)-2, len(cardPoints)-k-1, -1):
            back[i] = back[i+1] + cardPoints[i]
            best = back[i] # last one

        f = 0
        e = len(cardPoints)-k+1
        #print(front, back)

        for i in range(k-1):
            #print(f, e, best)
            best = max(best, front[f]+back[e])
            f += 1
            e += 1


        best = max(best, front[k-1])
        return best
