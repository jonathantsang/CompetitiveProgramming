class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        look = dict()
        for char in magazine:
            if char not in look:
                look[char] = 1
            else:
                look[char] = look[char] + 1
        for char in ransomNote:
            if char in look:
                if look[char] <= 0:
                    return False
                else:
                    look[char] = look[char] - 1
            else:
                return False
        return True