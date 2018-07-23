class Solution {
    vector<vector<int>> seen; // 0 not seen, 1 seen
    void dfs(vector<vector<char>>& grid, int y, int x){
        seen[y][x] = 1;
        // check direction if it is a 1 and not seen so far
        if(y-1 >= 0 && grid[y-1][x] == '1' && seen[y-1][x] == 0){
            dfs(grid, y-1, x);
        }
        if(y+1 < grid.size() && grid[y+1][x] == '1' && seen[y+1][x] == 0){
            dfs(grid, y+1, x);
        }
        if(x-1 >= 0 && grid[y][x-1] == '1' && seen[y][x-1] == 0){
            dfs(grid, y, x-1);
        }
        if(x+1 < grid[0].size() && grid[y][x+1] == '1' && seen[y][x+1] == 0){
            dfs(grid, y, x+1);
        }
    }
public:
    int numIslands(vector<vector<char>>& grid) {
        if(grid.size() == 0){
            return 0;
        }
        seen.resize(grid.size());
        for(int i = 0; i < seen.size(); i++){
            vector<int> row;
            row.resize(grid[0].size());
            seen[i] = row;
        }
        int islands = 0;
        for(int i = 0; i < grid.size(); i++){
            for(int j = 0; j < grid[i].size(); j++){
                if(seen[i][j] == 0 && grid[i][j] == '1'){
                    dfs(grid, i , j);
                    islands++;
                }
            }
        }
        return islands;
    }
};