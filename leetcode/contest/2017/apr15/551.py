class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lateCont = 0
        absent = 0
        for char in s:
            if(char == 'A'):
                absent += 1
                lateCont = 0
                if(absent > 1):
                    return False
            elif(char == 'L'):
                lateCont += 1
                if(lateCont > 2):
                    return False
            else:
                lateCont = 0
        return True