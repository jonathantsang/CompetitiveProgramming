class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        nextc = {'r' : 'c', 'o': 'r', 'a': 'o', 'k': 'a'}
        chars = {'c': 0, 'r': 0, 'o': 0, 'a': 0, 'k': 0}
        ans = 0
        for c in croakOfFrogs:
            #print(c, chars)
            if c == 'c':
                chars[c] += 1
            else:
                # check for completion
                placed = False
                want = nextc[c]
                if chars[want] > 0:
                    chars[want] -= 1
                    chars[c] += 1

                    # count simul
                    ans = max(ans, chars['c']+chars['r']+chars['o']+chars['a']+chars['k'])

                    if chars['k'] > 0:
                        chars['k'] -= 1
                else:
                    return -1
        # check all valid
        for d in ['c', 'r', 'o', 'a', 'k']:
            if chars[d] > 0:
                return -1
        return ans
