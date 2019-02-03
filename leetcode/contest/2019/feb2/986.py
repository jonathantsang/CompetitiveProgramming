# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# Plan


class Solution:
    def intervalIntersection(self, A: 'List[Interval]', B: 'List[Interval]') -> 'List[Interval]':
        values = {} # key value in A or B, value: array of [value, 'a' or 'b']
        
        for v in A:
            if v.start in values:
                values[v.start].append([1, 'a'])
            else:
                values[v.start] = [[1, 'a']]
            if v.end in values:
                values[v.end].append([-1, 'a'])
            else:
                values[v.end] = [[-1, 'a']]
        
        for v in B:
            if v.start in values:
                values[v.start].append([1, 'b'])
            else:
                values[v.start] = [[1, 'b']]
            if v.end in values:
                values[v.end].append([-1, 'b'])
            else:
                values[v.end] = [[-1, 'b']]
            
        # print(sorted(values.items()))
        
        avalue = 0 # 0 means it is closed, 1 means it is open
        bvalue = 0 # 0 means it is closed, 1 means it is open
        lasta = -1 # last value of A
        lastb = -1 # last value of B
        ans = [] # answer
        for number in sorted(values.keys()):
            for change in values[number]:
                if change[1] == 'a':
                    avalue += change[0]
                    lasta = number
                else:
                    bvalue += change[0]
                    lastb = number

                if lasta == -1 or lastb == -1:
                    continue
                if avalue == 0 and bvalue == 1 and lasta >= lastb:
                    ans.append([lastb, lasta])
                elif avalue == 1 and bvalue == 0 and lasta <= lastb:
                    ans.append([lasta, lastb])
        return ans
        