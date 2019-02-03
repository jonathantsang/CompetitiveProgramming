class Solution:
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        ans = ""
        larger = 'a'
        smaller = 'b'
        if A < B:
            larger = 'b'
            smaller = 'a'
        while A >= 1 or B >= 1:
            if A == B:
                ans += larger + smaller
                A -= 1
                B -= 1
            else:
                # complex
                if larger == 'a':
                    if A >= 2:
                        ans += 'aa'
                        A -= 2
                    elif A >= 1:
                        ans += 'a'
                        A -= 1
                    if B >= 1:
                        ans += 'b'
                        B -= 1
                else:
                    if B >= 2:
                        ans += 'bb'
                        B -= 2
                    elif B >= 1:
                        ans += 'b'
                        B -= 1
                    if A >= 1:
                        ans += 'a'
                        A -= 1
        return ans
                