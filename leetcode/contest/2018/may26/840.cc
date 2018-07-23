class Solution {
    bool checkValid(int i, int j, int k){
        if(min(i, min(j, k)) < 1 || max(i, max(j, k)) > 9){
            return false;
        }
        return true;
    }
    bool checkSquare(vector<vector<int>> &grid, int y, int x){
        // check rows grid[y][x], grid[y][x+1], grid[y][x+2]
        int magicSum = grid[y][x] + grid[y][x+1] + grid[y][x+2];
        for(int c = 0; c < 3; c++){
            if(!checkValid(grid[y+c][x], grid[y+c][x+1], grid[y+c][x+2])){
                return false;
            }
            int rowSum = grid[y+c][x] + grid[y+c][x+1] + grid[y+c][x+2];
            if(rowSum != magicSum){
                // cout << "fail row " << c << endl;
                return false;
            }
        }
        // check columns grid[y][x], grid[y+1][x], grid[y+2][x]
        for(int c = 0; c < 3; c++){
            if(!checkValid(grid[y][x+c], grid[y+1][x+c], grid[y+2][x+c])){
                return false;
            }
            int colSum = grid[y][x+c] + grid[y+1][x+c] + grid[y+2][x+c];
            if(colSum != magicSum){
                // cout << "fail col " << c << endl;
                return false;
            }
        }
        // check diagonals grid[y][x], grid[y+1][x+1], grid[y+2][x+2]
        // and grid[y][x+2], grid[y+1][x+1], grid[y+2][x]
        if(!checkValid(grid[y][x], grid[y+1][x+1], grid[y+2][x+2])){
            return false;
        }
        if(!checkValid(grid[y][x+2], grid[y+1][x+1], grid[y+2][x])){
            return false;
        }
        int d1Sum = grid[y][x] + grid[y+1][x+1] + grid[y+2][x+2];
        int d2Sum = grid[y][x+2] + grid[y+1][x+1] + grid[y+2][x];
        if(d1Sum != magicSum || d2Sum != magicSum){
            // cout << "fail diag" << endl;
            return false;
        }
        // all pass
        return true;
    }
public:
    int numMagicSquaresInside(vector<vector<int>>& grid) {
        int amt = 0;
        if(grid.size() < 3){
            return amt;
        }
        if(grid[0].size() < 3){
            return amt;
        }
        for(int i = 0; i < grid.size()-2; i++){
            for(int j = 0; j < grid[i].size()-2; j++){
                // cout << "test " << i << " " << j << endl;
                bool square = checkSquare(grid, i, j);
                if(square) amt++;
            }
        }
        return amt;
    }
};