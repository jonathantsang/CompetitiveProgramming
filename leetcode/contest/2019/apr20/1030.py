class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        queue = [(r0, c0)]
        ans = []
        seen = {} # Key: (r, c) tuple of coordinates, Value: 1
        while(len(queue) != 0):
            # print(queue)
            coord = queue.pop(0)
            
            if coord in seen:
                continue
            
            ans.append([coord[0], coord[1]])
            seen[coord] = 1
            
            # Look up, down, left right if not in seen, add to the queue
            # (y, x)
            up = (coord[0]-1, coord[1])
            down = (coord[0]+1, coord[1])
            right = (coord[0], coord[1]+1)
            left = (coord[0], coord[1]-1)
            if up not in seen and up[0] >= 0:
                queue.append(up)
            if down not in seen and down[0] < R:
                queue.append(down)
            if right not in seen and right[1] < C:
                queue.append(right)
            if left not in seen and left[1] >= 0:
                queue.append(left)
        return ans