class Solution {
public:
    int maxIncreaseKeepingSkyline(vector<vector<int>>& grid) {
        vector<int> row_max;
        vector<int> col_max;
        
        int width = grid[0].size();
        int height = grid.size();
        row_max.resize(height);
        col_max.resize(width);
        
        // Look for highest for rows;
        for(int i = 0; i < height; i++){
            // Each row
            int msf = grid[i][0];
            for(int j = 1; j < grid[i].size(); j++){
                msf = max(msf, grid[i][j]);
            }
            row_max[i] = msf;
        }
        
        // cout << "a" << endl;
        
        // Look for highest for columns
        for(int i = 0; i < width; i++){
            // Each row
            int msf = grid[0][i];
            for(int j = 1; j < height; j++){
                msf = max(msf, grid[j][i]);
            }
            col_max[i] = msf;
        }
        
        /*
        for(auto i : row_max){
            cout << i << " ";
        }
        cout << endl;
        
        for(auto i : col_max){
            cout << i << " ";
        }
        cout << endl;
        */
        
        // Update grid to lowest max for coordinate
        int total = 0;
        for(int i = 0; i < height; i++){
            for(int j = 0; j < width; j++){
                int temp = grid[i][j];
                grid[i][j] = min(row_max[i], col_max[j]);
                total += (grid[i][j] - temp);
            }
        }
        
        return total;
    }
};