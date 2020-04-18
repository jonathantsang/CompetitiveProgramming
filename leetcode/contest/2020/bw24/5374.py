class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if k > 3 * 2**(n-1):
            return ""
        word = []
        small = 1
        large = 3 * 2**(n-1)
        if k >= 2 * 2**(n-1)+1:
            word.append('c')
            small += 2 * 2**(n-1)
        elif k >= 1 * 2**(n-1)+1:
            word.append('b')
            small += 1 * 2**(n-1)
            large -= 1 * 2**(n-1)
        else:
            word.append('a')
            large -= 2 * 2**(n-1)
        # print(n, k, "case")
        while len(word) < n:
            #print(small, large)
            #print(word)
            larger = False
            mid = (small + large) // 2
            if k > mid:
                larger = True
            
            if not larger:
                if word[-1] == 'a':
                    word.append('b')
                elif word[-1] == 'b':
                    word.append('a')
                elif word[-1] == 'c':
                    word.append('a')
            else:
                if word[-1] == 'a':
                    word.append('c')
                elif word[-1] == 'b':
                    word.append('c')
                elif word[-1] == 'c':
                    word.append('b')
                    
            # change k
            if larger:
                small = mid + 1
            else:
                large = mid
            #print(word)
        return "".join(word)
            
        