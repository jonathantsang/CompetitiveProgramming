class Solution:
    seen = {}
    equals = {} # key: character, value: [{equal characters}, {not equal characters}]

    # Can it c1 equal c2
    def checksets(self, cur, c1, c2, equal):
        if cur in self.seen:
            return False
        self.seen[cur] = 1
        # Want to check
        if equal:
            # c2 in the not set of current
            if c2 in self.equals[cur][1]:
                return True
            # for each char same as me
            for same in self.equals[cur][0]:
                v = self.checksets(same, c1, c2, equal)
                if v == True:
                    return True
        else:
            # c2 not in the set of current
            if c2 in self.equals[cur][0]:
                return True
            # for each char same as me
            for same in self.equals[cur][0]:
                v = self.checksets(same, c1, c2, equal)
                if v == True:
                    return True
        return False
            
    
    def equationsPossible(self, equations: 'List[str]') -> 'bool':
        self.seen = {}
        self.equals = {}
        for e in equations:
            if e[1] == '=':
                c1 = e[0]
                c2 = e[3]
                
                if c1 in self.equals:
                    self.equals[c1][0][c2] = 1
                else:
                    self.equals[c1] = [{c2: 1}, {}]
                
                if c2 in self.equals:
                    self.equals[c2][0][c1] = 1
                else:
                    self.equals[c2] = [{c1: 1}, {}]
                
            else:
                c1 = e[0]
                c2 = e[3]
                
                if c1 == c2:
                    return False
                
                if c1 in self.equals:
                    self.equals[c1][1][c2] = 1
                else:
                    self.equals[c1] = [{}, {c2: 1}]
                
                if c2 in self.equals:
                    self.equals[c2][1][c1] = 1
                else:
                    self.equals[c2] = [{}, {c1: 1}]
        
        # print(self.equals)
        for e in equations:
            self.seen = {}
            c1 = e[0]
            c2 = e[3]
            v = self.checksets(c1, c1, c2, e[1] == '=')
            if v == True: # Trouble
                return False
                
        return True