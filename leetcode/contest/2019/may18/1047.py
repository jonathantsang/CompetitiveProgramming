class Solution:
    def removeDuplicates(self, S: str) -> str:
        while(True):
            leng = len(S)
            for c in range(97, 123):
                rem = chr(c) + chr(c)
                #print(rem)
                S = S.replace(rem, '')
            #print(S)
            if len(S) == leng:
                break
        return S