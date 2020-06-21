class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        stored = defaultdict(set) # name -> set suffix taken
        LENG = 1000000

        ans = []
        for n in names:
            #print(n)
            minimum = -1
            if n in stored:
                for i in range(-1, LENG):
                    if i not in stored[n]:
                        minimum = i
                        break
            if minimum == -1:
                ans.append(n)
                stored[n].add(-1)
                stored[n].add(0)
            else:
                constructed = n + '(' + str(minimum) + ')'
                ans.append(constructed)
                stored[n].add(minimum)
                stored[constructed].add(0)
                stored[constructed].add(-1)

            n = list(n)

            if n[-1] == ')':
                temp = deque()
                while n[-1] != '(':
                    char = n[-1]
                    temp.appendleft(char)
                    n.pop()
                n.pop() # pop bracket '('
                #print(temp)
                #print("add ", "".join(n), "amt,", int("".join([temp[i] for i in range(len(temp)-1)])))
                newnumber = int("".join([temp[i] for i in range(len(temp)-1)]))
                if newnumber == 0:
                    # not a (0) for some string
                    pass
                else:
                    stored["".join(n)].add(newnumber)
        return ans




                
