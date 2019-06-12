# clumsy
# * / + -
# 4 * 3 / 2 + 1
# 7
# 5 * 4 / 3 + 2 - 1
# 6 + 2 - 1 = 7
# 6 * 5 / 4 + 3 - 2 * 1
# 7 + 3 - 2 = 8

# 10 * 9 / 8 + 7 
# - 6 * 5 / 4 + 3 
# - 2 * 1

class Solution:
    def clumsy(self, N: int) -> int:
        total = 0
        front = -1
        for i in range(N, -1, -4):
            if i == N:
                front = 1
            else:
                front = -1
                
            if i > 3:
                total += front * (i * (i - 1) // (i - 2)) + (i - 3)
            elif i == 3:
                total += front * (i * (i - 1) // (i - 2))
            elif i == 2:
                total += front * (i * (i - 1))
            elif i == 1:
                total += front * i
        return total