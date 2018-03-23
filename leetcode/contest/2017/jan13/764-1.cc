class Solution {
    vector<vector<int>> grid;
    vector<vector<int>> data;
    vector<vector<int>> left; // How much more straight left
    vector<vector<int>> up; // How much more straight up
    vector<vector<int>> right; // How much more straight left
    vector<vector<int>> down; // How much more straight up
    
    int CheckSpot1(int x, int y){
        // get left and up
        if(y-1 < 0 && x-1 < 0){
            up[y][x] = grid[y][x];
            left[y][x] = grid[y][x];
            data[y][x] = grid[y][x];
            return 0;
        } else if(y-1 < 0){
            up[y][x] = grid[y][x];
            left[y][x] = left[y][x-1];
            data[y][x] = grid[y][x];
            return 0;
        } else if(x-1 < 0){
            up[y][x] = up[y-1][x];
            left[y][x] = grid[y][x];
            data[y][x] = grid[y][x];
            return 0;
        }
        // Else use the values
        up[y][x] = up[y-1][x];
        left[y][x] = left[y][x-1];
        data[y][x] = grid[y][x];
        return grid[y][x];
    }
    
    int CheckSpot2(int x, int y){
        // get right and down
        if(y+1 >= grid.size() && x+1 >= grid.size()){
            down[y][x] = grid[y][x];
            right[y][x] = grid[y][x];
            data[y][x] = grid[y][x]; // New
            return grid[y][x];
        } else if (y+1 >= grid.size()){
            down[y][x] = grid[y][x];
            right[y][x] = right[y][x+1];
            data[y][x] = grid[y][x]; // New
            return grid[y][x];
        } else if (x+ 1 >= grid.size()){
            down[y][x] = down[y+1][x];
            right[y][x] = grid[y][x];
            data[y][x] = grid[y][x]; // New
            return grid[y][x];
        }
        // Else use the values
        down[y][x] = down[y+1][x];
        right[y][x] = right[y][x+1];
        data[y][x] = min(min(down[y][x], left[y][x]), min(right[y][x], up[y][x])) + grid[y][x];
        return data[y][x];
    }
    
public:
    int orderOfLargestPlusSign(int N, vector<vector<int>>& mines) {
        grid.clear();
        left.clear();
        up.clear();
        down.clear();
        right.clear();
        data.clear();
        for(int i = 0; i < N; i++){
            vector<int> row;
            row.resize(N);
            fill(row.begin(), row.end(), 1);
            grid.emplace_back(row);
            
            // left
            vector<int> lrow;
            lrow.resize(N);
            fill(lrow.begin(), lrow.end(), 0);
            left.emplace_back(lrow);
            
            // up
            vector<int> urow;
            urow.resize(N);
            fill(urow.begin(), urow.end(), 0);
            up.emplace_back(urow);
            
            // right
            vector<int> rrow;
            rrow.resize(N);
            fill(rrow.begin(), rrow.end(), 0);
            right.emplace_back(rrow);
            
            // down
            vector<int> drow;
            drow.resize(N);
            fill(drow.begin(), drow.end(), 0);
            down.emplace_back(drow);
            
            // data
            vector<int> ddrow;
            ddrow.resize(N);
            fill(ddrow.begin(), ddrow.end(), 0);
            data.emplace_back(ddrow);
            
        }
        // Input mines
        for(int i = 0; i < mines.size(); i++){
            int x = mines[i][0];
            int y = mines[i][1];
            grid[y][x] = 1;
        }
        
        // Check each spot for plus
        int max = 0;
        // Left and down
        for(int i = 0; i < grid.size(); i++){
            for(int j = 0; j < grid[i].size(); j++){
                int val = CheckSpot1(j, i);
                if(val > max){
                    max = val;
                }
            }
        }
        // Right and Up
        for(int i = grid.size()-1; i > -1; --i){
            for(int j = grid[i].size()-1; j > -1; --j){
                int val = CheckSpot2(j, i);
                if(val > max){
                    max = val;
                }
            }
        }
        return max;
    }
};