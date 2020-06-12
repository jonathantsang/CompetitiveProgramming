class Fenwick():
    def __init__(self, arr):
        self.N = len(arr)
        self.BIT = [0 for _ in range(self.N+1)]

        for i in range(self.N):
            self.update(i, arr[i])

    def update(self, i, val):
        index = i+1

        while index <= self.N:
            self.BIT[index] += val

            index += index & (-index)

    # Gets sum of first n values
    def getSum(self, n):
        sum = 0
        index = n

        while index > 0:
            sum += self.BIT[index]
            index -= index & (-index)

        return sum

    def __repr__(self):
        return " ".join(list(map(str, self.BIT)))

    def __str__(self):
        return " ".join(list(map(str, self.BIT)))

# Small test
# f = Fenwick([2,1,1,3,2,3,4,5,6,7,8,9])
# print(f)
# print(f.getSum(3) == 4)
# print(f.getSum(7) == 16)
# print(f.getSum(9) == 27)
