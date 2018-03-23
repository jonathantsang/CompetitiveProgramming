class Solution {
    vector<vector<int>>totals;
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        totals.clear();
        int leng = grid.size();
        // Make totals to store everything so far in search, up and left
        for(int i = 0; i < leng; i++){
            vector<int> row;
            int sizeWanted = grid[i].size();
            row.resize(sizeWanted);
            totals.emplace_back(row);
        }
        // Construct totals
        int maxSoFar = 0;
        // Go to each row finding the largest contiguous block
        for(int i = 0; i < leng; i++){
            int lengOfRow = grid[i].size();
            int total = 0;
            int start = 0;
            vector<int> indices;
            // Each vertice in the row
            for(int j = 0; j < lengOfRow; j++){
                if(grid[i][j] == 0){
                    for(int p = start; p < j; p++){
                        grid[i][p] = total;
                    }
                    start = -1;
                    total = 0;
                } else if (grid[i][j] != 0){
                    if(start == -1){
                        start = j;
                    }
                    total += grid[i][j];
                }
            }
            if(start != -1){
                for(int p = start; p < lengOfRow; p++){
                    grid[i][p] = total;
                }
                start = -1;
                total = 0; 
            }
            
            // Dump previous vertices on next row if it has a 1
            int height = grid.size();
            for(int j = 0; j < lengOfRow; j++){
                if(i+1 >= grid.size()){
                    break;
                }
                if(grid[i+1][j] != 0){
                    grid[i+1][j] += grid[i][j];
                }
            }
            
            for(int j = 0; j < lengOfRow; j++){
                if(grid[i][j] > maxSoFar){
                    maxSoFar = grid[i][j];
                }
            }
        
            
            /* Print
            for(int i = 0; i < leng; i++){
                int lengOfRow = grid[i].size();
                // Each vertice in the row
                for(int j = 0; j < lengOfRow; j++){
                    cout << grid[i][j];
                }
                cout << endl;
            }*/
        }
            
        return maxSoFar;
    }
};