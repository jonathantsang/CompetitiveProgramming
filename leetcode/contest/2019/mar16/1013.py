class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # print(count)
        total = 0
        count = {} # Key: duration, Value: count
        for t in time:
            if t in count:
                count[t] += 1
            else:
                count[t] = 1
        for key1 in count:
            for key2 in count:
                # print(key1, key2)
                if key1 == key2 and count[key1] >= 2 and (key1 + key2) % 60 == 0:
                    total += count[key1] * (count[key2] - 1)
                elif key1 != key2 and (key1 + key2) % 60 == 0:
                    total += count[key1] * count[key2]
                # print(total)
        return total // 2