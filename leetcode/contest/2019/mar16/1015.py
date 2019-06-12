class Solution:
    def checkrepeated(self, num):
        a = {}
        while num != 0:
            d = num % 10
            
            if d in a:
                return True
            
            a[d] = 1
            
            num //= 10
            
        return False
            
    def numDupDigitsAtMostN(self, N: int) -> int:
        amt = 0
        for i in range(0, N+1):
            if self.checkrepeated(i):
                amt += 1
                # print(i)
        return amt