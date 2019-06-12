class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        if N == 1:
            return 0
        binary = ""
        while N > 0:
            res = N // 2
            remainder = N % 2
            binary += str(remainder)
            N = res
        # print(binary)
        ans = ""
        for c in binary:
            if c == '1':
                ans += '0'
            else:
                ans += '1'
        # print(ans)
        ans = ans[::-1]
        # print(ans)
        final = 0
        j = 1
        for i in range(len(ans)-1, -1, -1):
            #print(i, d)
            if str(ans[i]) == '1':
                if len(ans)-1 == i:
                    final += 1
                else:
                    final += j
            j *= 2
        return final
        