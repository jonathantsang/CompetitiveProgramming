class Solution:

    def __init__(self, w: List[int]):
        n = 0
        arr = []
        for i in w:
            n += i
            arr.append(n)
        self.arr = arr
        self.max = n
        print(self.arr)

    def pickIndex(self) -> int:
        n = randrange(self.max)
        return bisect_right(self.arr, n)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
