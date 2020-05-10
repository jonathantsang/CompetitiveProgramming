import collections

class Solution:
    def solve(self, matrix):
        
        def traverse(i, j, travel):
            leng = 30
            queue = collections.deque([(i, j, 0)])
            if travel[i][j] == float('inf'):
                travel[i][j] = 0 # takes this person 0 steps to go there
            while len(queue) > 0:
                v = queue.popleft()
                print(v)
                if v[2] > leng:
                    continue
                if travel[v[0]][v[1]] == float('inf'):
                    travel[v[0]][v[1]] = v[2]    
                else:
                    travel[v[0]][v[1]] += v[2]
                for y, x in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    ny = v[0]+y
                    nx = v[1]+x
                    if ny < 0 or nx < 0 or ny == len(matrix) or nx == len(matrix[0]):
                        continue
                    if matrix[ny][nx] != 1:
                        queue.append((ny, nx, v[2]+1))
            
        
        # Write your code here
        travel = [[float('inf')] * len(matrix[0])] * len(matrix)
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if matrix[i][j] == 2:
                    traverse(i, j, travel)
                    return travel