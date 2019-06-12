class Solution(object):
    all = []
    
    def permutate(i, lengths, cur):
        if i == len(lengths):
            self.all.append(cur)
        for j in range(0, lengths[i]):
            permutate(i+1, lengths, cur+str(j))
    
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.all = []
        mapping = {}
        for i in range(2, 7):
            mapping[i] = []
            for j in range(0, 3):
                mapping[i].append(chr(ord('a')+j+3*(i-2)))
        mapping[7] = ['p', 'q', 'r', 's']
        mapping[8] = ['t', 'u', 'v']
        mapping[9] = ['w', 'x', 'y', 'z']
        
        lengths = []
        # For n length number denoting index for each letter for each digit
        for d in digits:
            lengths.append(len(mapping[int(d)]))
        
        permutate(i, lengths, "")
        
        return self.all