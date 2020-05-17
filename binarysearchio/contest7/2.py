class Solution:
    def gcd(self, a, b):
        if (a == 0 or b == 0):
            return 0
        if (a == b):
            return a
        if (a > b):
            return self.gcd(a - b, b)
        return self.gcd(a, b - a)

    def solve(self, a, b):
        if a < b:
            a, b = b, a
        if self.gcd(a, b) != 1:
            return 0
        # even even
        if a % 2 == 0 and b % 2 == 0:
            return 0
        # odd, even
        if a % 2 != b % 2:
            return 1

        # odd, odd, can it decrement to divisor
        if self.gcd(a+1, b) != 1 or self.gcd(a-1, b) != 1:
            return 1
        if self.gcd(a, b+1) != 1 or self.gcd(a, b-1) != 1:
            return 1

        # else add +1 to each odd and make common div 2
        return 2
