class Solution {
    vector<vector<int>> grid;
    vector<vector<int>> left; // How much more straight left
    vector<vector<int>> up; // How much more straight up
    
    int CheckPlus(vector<int>&grid, int x, int y){
        // boundaries
        if(y-1 < 0){
            up[y][x] = 0;
            if(x-1 < 0){
                left[y][x] = 0;
            } else {
                left[y][x] = left[y][x-1];
            }
            return grid[y][x];
        }
        if(y+1 > grid.size()){
            up[y][x] = up[y-1][x];
            if(x-1 < 0){
                left[y][x] = 0;
            } else {
                left[y][x] = left[y][x-1];
            }
            return grid[y][x];
        }
        if(x+1 > grid.size()){
            if(y-1 < 0){
                up[y][x] = 0;
            } else {
               up[y][x] = up[y-1][x]; 
            }
            left[y][x] = left[y][x-1];
            return grid[y][x];
        }
        if(x-1 < 0){
            if(y-1 < 0){
                up[y][x] = 0;
            } else {
               up[y][x] = up[y-1][x]; 
            }
            left[y][x] = 0;
            return grid[y][x];
        }
        
        // Check up, down, left right
        int u = up[y-1][x]; // previous
        int down = grid[y+1][x]; 
        int right = grid[y][x+1];
        int l = left[y][x-1]; // previous
        
        up[y][x] = grid[y][x] + up;
        left[y][x] = grid[y][x] + l;
        
        
        
    }
    
public:
    int orderOfLargestPlusSign(int N, vector<vector<int>>& mines) {
        grid.clear();
        left.clear();
        up.clear();
        for(int i = 0; i < N; i++){
            vector<int> row;
            row.resize(N);
            fill(row.begin(), row.end(), 1);
            grid.emplace_back(row);
            
            // left
            vector<int> lrow;
            drow.resize(N);
            fill(lrow.begin(), urow.end(), 0);
            left.emplace_back(drow);
            
            // up
            vector<int> urow;
            urow.resize(N);
            fill(urow.begin(), urow.end(), 0);
            up.emplace_back(urow);
            
        }
        // Input mines
        for(int i = 0; i < mines.size(); i++){
            int x = mines[i][0];
            int y = mines[i][1];
            grid[y][x] = 1;
        }
        
        // Check each spot for plus
        int max = 0;
        for(int i = 0; i < grid.size(); i++){
            for(int j = 0; j < grid[i].size(); j++){
                int val = CheckSpot(grid, data);
                if(val > max){
                    max = val;
                }
            }
        }
        
        return max;
    }
};