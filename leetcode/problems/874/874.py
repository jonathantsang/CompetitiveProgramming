class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        y = 0
        x = 0
        d = 0 # n = 0, e = 1, s = 2, w = 3
        obs = {} # Key: tuple of coord (x,y), Value: 1
        ans = 0
        for o in obstacles:
            obs[(o[0],o[1])] = 1
        for c in commands:
            if c == -1:
                d = (d + 1) % 4
            elif c == -2:
                d -= 1
                if d == -1:
                    d = 3
            else:
                # print(y, x)
                for i in range(0, c):
                    if d == 0:
                        if (x, y+1) in obs:
                            break
                        y += 1
                    elif d == 1:
                        if (x+1, y) in obs:
                            break
                        x+=1
                    elif d == 2:
                        if (x, y-1) in obs:
                            break
                        y-=1
                    elif d == 3:
                        if (x-1, y) in obs:
                            break
                        x-=1
                    ans = max(ans, pow(y, 2) + pow(x, 2))
        return ans