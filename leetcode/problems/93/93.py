class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.all = []
        self.seen = {} # Key: number -> Value: 1
        for i in range(1, 4):
            for j in range(1, 4):
                for k in range(1, 4):
                    for l in range(1, 4):
                        ans = s[:i] + '.' + s[i:i+j] + '.' + s[i+j:i+j+k] + '.' + s[i+j+k:i+j+k+l]
                        if len(ans) == len(s) + 3:
                            # Check 255 max number
                            a = ans.split('.')
                            valid = True
                            for part in a:
                                if part == '':
                                    valid = False
                                elif len(part) > 1 and part[0] == '0':
                                    valid = False
                                elif int(part) > 255:
                                    valid = False
                            if valid and ans not in self.seen:
                                self.seen[ans] = 1
                                self.all.append(ans)
        return self.all