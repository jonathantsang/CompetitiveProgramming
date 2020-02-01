class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True
        stackleft = []
        stackright = []
        stackempty = []
        left = True
        right = True
        empty = True
        for i in range(0, len(s)):
            if s[i] == "(":
                stackleft.append("(")
                stackright.append("(")
                stackempty.append("(")
            elif s[i] == ")":
                if len(stackleft) != 0 and stackleft[-1] == "(":
                    stackleft.pop()
                else:
                    left = False
                if len(stackright) != 0 and stackright[-1] == "(":
                    stackright.pop()
                else:
                    right = False
                if len(stackempty) != 0 and stackempty[-1] == "(":
                    stackempty.pop()
                else:
                    empty = False
                
            else:
                stackleft.append("(")
                
                if len(stackright) != 0 and stackright[-1] == "(":
                    stackright.pop()
                else:
                    right = False
        
        print(left, stackleft)
        print(right, stackright)
        print(empty, stackempty)
        return (left and len(stackleft) == 0) or (right and len(stackright) == 0) or (empty and len(stackempty) == 0)