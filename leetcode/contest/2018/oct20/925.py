class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i = 0
        j = 0
        while(i < len(name) and j < len(typed)):
            if name[i] == typed[j]:
                char = typed[j]
                count = 0
                while j < len(typed) and typed[j] == char:
                    count += 1
                    j += 1
                nameC = 0
                while i < len(name) and name[i] == char:
                    nameC += 1
                    i += 1
                if nameC > count:
                    return False
            else:
                return False
        if i == len(name):
            return True
        return False