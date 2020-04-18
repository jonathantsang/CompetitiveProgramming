class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib = [1, 1, 2]
        while fib[-1] + fib[-2] <= k:
            fib.append(fib[-1] + fib[-2])
        ans = 0
        for i in range(len(fib)-1, -1, -1):
            if fib[i] <= k:
                k -= fib[i]
                ans += 1
            if k == 0:
                break
        return ans