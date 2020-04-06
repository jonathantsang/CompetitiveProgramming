class Solution:
    def numSteps(self, s: str) -> int:
        num = 0
        j = 0
        for i in range(len(s)-1, -1, -1):
            num += int(s[i]) * 2**j
            j += 1
        #print(num)
        steps = 0
        while num != 1:
            #print(num)
            if num % 2:
                num += 1
            else:
                num //= 2
            steps += 1
        return steps