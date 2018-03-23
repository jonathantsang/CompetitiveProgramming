class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        newA = a.split("+")
        newB = b.split("+")
        c = int(newA[0])
        d = int(newB[0])
        e = newA[1].split("-")
        f = newB[1].split("-")
        
        if(e[0] == ""):
            e = e[1][0]
        else:
            e = e[0][0]
        if(f[0] == ""):
            f = f[1][0]
        else:
            e = e[0][0]
            
        p1 = c * e 
        p2 = c * f
        p3 = d * e 
        ## p4 = e * f
        ## Check if the same, otherwise 0
        p2p3 = 0
        if(p2 == p3):
            if(p2[0] == "-"):
                p2p3 = "-2i"
            else:
                p2p3 = "2i"
        ## One is negative and one isn't
        if((e[0] == "-" and f[0] != "-") or (e[0] != "-" and f[0] == "-")):
            p4 = "-1"
        else:
            p4 = "1"
        p1p4 = str(int(p1) + int(p4))
        return p1p4 + "+" + p2p3
        
        
        