class Solution {
    pair<int, int> getMove(int x, int y, int dir){
        if(dir == 0){
            // right
            x++;
        } else if (dir == 1){
            y--;
        } else if (dir == 2){
            x--;
        } else if (dir == 3){
            y++;
        }
        pair<int, int> p;
        p.first = x;
        p.second = y;
        return p;
    }
    
    bool validMove(int x, int y, int dir, int R, int C){
        // y constraints 0 to R-1
        // x constraints 0 to C-1
        if(dir == 0){
            // right
            x++;
        } else if (dir == 1){
            y--;
        } else if (dir == 2){
            x--;
        } else if (dir == 3){
            y++;
        }
        return validSpot(x, y, R, C);
    }
    
    bool validSpot(int x, int y, int R, int C){
        if((x >= 0 && x <= (C-1)) && (y >= 0 && y <= (R-1))){
            return true;
        } else {
            return false;
        }
    }
    
    void updateMove(int& x, int& y, int& dir, int R, int C, vector<vector<int>> &grid){
        if(validMove()){
            
            // NEED THE CHECK IF OCCUPIED
            if(dir == 0){
            // right
                x++;
            } else if (dir == 1){
                y--;
            } else if (dir == 2){
                x--;
            } else if (dir == 3){
                y++;
            }
            // no need to return the reference
            dir++;
            dir %= 4;
        } else {
            // have to do lookup one direction after
            bool placed = false;
            while(!placed){
                // Check outside bounds
                if(x < 0 || x >= C || y < 0 || y >= R){
                    dir++;
                    dir %= 4;
                }
            }
            
            // works
            grid[y][x] = 1;
            
        }
    }
    
public:
    vector<vector<int>> spiralMatrixIII(int R, int C, int r0, int c0) {
        int dir = 0; // 0 right, 1 down, 2 left, 3 up
        int covered = 0;
        int x = c0;
        int y = r0;
        vector<vector<int>> grid(R, vector<int>(0,C));
        vector<vector<int>> coords;
        while(covered < R * C){
            // mark as seen
            grid[y][x] = 1;
            
            // move and dir
            updateMove(x, y, dir, R, C, grid);
                        
            covered++;
        }
    }
};