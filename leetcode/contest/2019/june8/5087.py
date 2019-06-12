class Solution:
    seen = {} # Key: strings, Value: 1
    def form(self, string, tiles, used):
        self.seen[string] = 1
        for i in range(0, len(tiles)):
            if i not in used:
                used[i] = 1
                self.form(string+tiles[i], tiles, used)
                del used[i]

    def numTilePossibilities(self, tiles: str) -> int:
        self.seen = {}
        used = {}
        self.form("", tiles, used)
        return len(self.seen)-1 # minus 1 for ""
        