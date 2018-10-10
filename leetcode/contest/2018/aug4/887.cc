class Solution {
public:
    int projectionArea(vector<vector<int>>& grid) {
        int top = 0;
        int front = 0;
        int side = 0;
        vector<vector<int>> topdowngrid(50, vector<int>(50, 0));
        
        // top
        for(int i = 0; i < grid.size(); i++){
            // y
            for(int j = 0; j < grid[0].size(); j++){
                topdowngrid[j][i] = grid[i][j]; 
                if(grid[i][j] != 0){
                    top++;
                }
            }
        }
        
        // front
        // Each row
        for(int i = 0; i < grid.size(); i++){
            // each column in row get the max
            int colmax = 0;
            for(int j = 0; j < grid[0].size(); j++){
                colmax = max(grid[i][j], colmax);
            }
            front += colmax;
        }
        
        // side
        // Each column
        for(int j = 0; j < grid.size(); j++){
            // each row in column get the max
            int rowmax = 0;
            for(int i = 0; i < grid[0].size(); i++){
                rowmax = max(grid[i][j], rowmax);
            }
            side += rowmax;
        }
        
        return top + front + side;
    }
};