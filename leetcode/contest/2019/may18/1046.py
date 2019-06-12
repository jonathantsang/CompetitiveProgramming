class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while(len(stones) > 1):
            largest = [stones[0], 0]
            second = [stones[1], 1]
            if stones[0] < stones[1]:
                largest = [stones[1], 1]
                second = [stones[0], 0]
                
            #print("start", stones, largest, second)
            for i, stone in enumerate(stones):
                # Start at 2 since largest and second are 0, and 1
                if i < 2:
                    continue
                if stone > largest[0]:
                    second = largest
                    largest = [stone, i]
                elif stone > second[0]:
                    second = [stone, i]
            # Smash largest and second
            if largest[0] == second[0]:
                # Pop greater first so it doesn't mess it up
                if largest[1] > second[1]:
                    stones.pop(largest[1])
                    stones.pop(second[1])
                else:
                    stones.pop(second[1])
                    stones.pop(largest[1])
            else:
                stones[largest[1]] -= second[0]
                stones.pop(second[1])
            #print(stones, largest, second)
        if len(stones) == 0:
            return 0
        else:
            return stones[0]