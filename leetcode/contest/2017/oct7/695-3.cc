class Solution {
    vector<vector<int>> performed;
    vector<vector<int>> visited;
    int total;
    int maxTotal;
public:
    void makeVisited(int heightLen, int rowLen){
        // Make visited
        for(int p = 0; p < heightLen; p++){
            for(int v = 0; v < rowLen; v++){
                vector<int> row;
                fill(row.begin(), row.end(), 0);
                row.resize(rowLen);
                visited.emplace_back(row);
            }
        }
    }
    
    void makePerformed(int heightLen, int rowLen){
        // Make visited
        for(int p = 0; p < heightLen; p++){
            for(int v = 0; v < rowLen; v++){
                vector<int> row;
                fill(row.begin(), row.end(), 0);
                row.resize(rowLen);
                performed.emplace_back(row);
            }
        }
    }
    
    void dfs(int x, int y, vector<vector<int>>& grid){
        
        int maxH = grid.size();
        int maxW = grid[0].size();
        
        total += grid[y][x];
        visited[y][x] = 1;
        performed[y][x] = 1;

        // Check up, right, down, left
        if((y+1 < maxH) && visited[y+1][x] != 1 && grid[y+1][x] == 1){
            dfs(x, y+1, grid);
        }
        if((x+1 < maxW) && visited[y][x+1] != 1 && grid[y][x+1] == 1){
            dfs(x+1, y, grid);
        }
        if((y-1 >= 0) && visited[y-1][x] != 1 && grid[y-1][x] == 1){
            dfs(x, y-1, grid);
        }
        if((x-1 >= 0) && visited[y][x-1] != 1 && grid[y][x-1] == 1){
            dfs(x-1, y, grid);
        }        
    }
    
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        visited.clear();
        performed.clear();
        total = 0;
        maxTotal = 0;
        int heightLen = grid.size();
        int rowLen = grid[0].size();
        
        makeVisited(heightLen, rowLen);
        makePerformed(heightLen, rowLen);
        
        // DFS on 1
        for(int i = 0; i < heightLen; i++){
            for(int j = 0; j < rowLen; j++){
                if(grid[i][j] == 1 && performed[i][j] != 1){                    
                    dfs(j,i, grid);
                    if(total > maxTotal){
                        maxTotal = total;   
                    }
                    total = 0;
                    performed[i][j] = 1;
                }
            }
        }
        return maxTotal;
    }
    
    
};