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
    bool validSpot(int x, int y, int R, int C){
        if((x >= 0 && x <= (C-1)) && (y >= 0 && y <= (R-1))){
            return true;
        } else {
            return false;
        }
    }
public:
    vector<vector<int>> spiralMatrixIII(int R, int C, int r0, int c0) {
        int dir = 0; // 0 right, 1 down, 2 left, 3 up
        int covered = 0;
        vector<vector<int>> coords;
        vector<vector<int>> grid(R, vector<int>(C, 0));
        int x = c0;
        int y = r0;
        vector<int> fi;
        fi.push_back(y);
        fi.push_back(x);
        grid[y][x] = 1;
        coords.push_back(fi);
        covered++;
        while(covered < R*C){
            // cout << y << " " << x << endl;
            // Move in direction
            pair<int, int> p = getMove(x, y, dir);
            if(validSpot(p.first, p.second, R, C) && grid[p.second][p.first] == 0){
                // mark it and move there
                grid[p.second][p.first] = 1;
                x = p.first;
                y = p.second;
                covered++;
                vector<int> pos;
                pos.push_back(y);
                pos.push_back(x);
                coords.push_back(pos);
                
                dir++;
                dir %= 4;
            } else if (validSpot(p.first, p.second, R, C) && grid[p.second][p.first] == 1) {
                if(!validSpot(p.first, p.second, R, C)){
                    dir++;
                    dir %= 4;
                    continue; // keep looking in the dir    
                } else {
                    // Same dir, keep moving
                    x = p.first;
                    y = p.second;
                    continue;
                }
            } else {
                // edge switch dir
                dir++;
                dir %= 4;
            }
        }
        return coords;
    }
};