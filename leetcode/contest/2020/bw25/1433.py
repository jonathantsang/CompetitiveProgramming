class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s3 = sorted(s1)
        s4 = sorted(s2)

        b = True
        #print(s4, s3)
        for i in range(len(s3)):
            #print(s3[i], s4[i])
            #print(ord(s3[i]), ord(s4[i]))
            if s3[i] < s4[i]:
                b = False
                break

        if b:
            return b

        b = True
        s3, s4 = s4, s3
        for i in range(len(s3)):
            #print(s3[i], s4[i])
            #print(ord(s3[i]), ord(s4[i]))
            if s3[i] < s4[i]:
                b = False
                break

        return b
