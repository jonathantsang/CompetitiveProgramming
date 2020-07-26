class Solution:
    def solve(self, a, b):
        def check(a,b):
            N,M=len(a),len(b)
            i,j=0,M-1
            swap = False

            # palindrome check
            for _ in range(M//2):
                if swap:
                    if not a[i] == a[j]:
                        return False
                if not a[i] == b[j]:
                    if a[i] == a[j]:
                        swap = True
                    else:
                        return False
                i+=1
                j-=1
            return True

        return check(a,b) or check(b,a)
