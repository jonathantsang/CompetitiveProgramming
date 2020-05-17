def solve(self, A):
        N = len(A)
        powers = [0]
        P = [0]
        p = 0
        s = 0
        for i, x in enumerate(A, 1):
            p += i * x
            s += x
            powers.append(p)
            P.append(s)

        ans = power =  powers[-1]
        #print("!", power)
        for i, x in enumerate(A):
            # we move x somewhere
            for j in range(N + 1):
                if j < i:
                    power2 = power + P[i] - P[j] - (i - j) * x
                    if power2 > ans: ans = power2
                elif j >= i:
                    #if i == 0 and j == 2:
                        #print("a!", P[j + 1] - P[i + 1], j - i)
                    power2 = power + P[i] - P[j] - (i - j) * x
                    if power2 > ans: ans = power2
        return ans

# from awice
