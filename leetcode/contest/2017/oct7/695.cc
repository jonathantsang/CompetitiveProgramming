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
        for(int i = 0; i < leng; i++){
            int lengOfRow = grid[i].size();
            for(int j = 0; j < lengOfRow; j++){
                // If it is 0, it is 0 size
                if(grid[i][j] == 0){
                    totals[i][j] = 0;
                } else if (grid[i][j] == 1){
                    // Else get top and left amounts (within the indices)
                    // Starts at 1 since the grid[i][j] has a 1
                    int addedSize = 1;
                    // One in the above row
                    if(i - 1 >= 0){
                        addedSize += totals[i-1][j];
                    }
                    totals[i][j] = addedSize;
                }
            }
        }
        // Update each element above it contiguously
        int lengOfRow = totals[0].size();
        int height = totals.size();
        for(int j = lengOfRow -1; j >= 0; j--){
            int maxForCol = 0;
            for(int i = height - 1; i >= 0; i--){
                if(totals[i][j] > maxForCol){
                    maxForCol = totals[i][j];
                } else if(totals[i][j] != 0 && totals[i][j] < maxForCol){
                    // Update for contiguous amount (possible max)
                    totals[i][j] = maxForCol;
                } else if (totals[i][j] == 0) {
                    // Contiguous ended
                    maxForCol = 0;
                }
            }
        }
        // Go to each row finding the largest contiguous block
        for(int i = 0; i < leng; i++){
            int lengOfRow = totals[i].size();
            int total = 0;
            for(int j = 0; j < lengOfRow; j++){
                // End total and check if largest
                if(totals[i][j] == 0){
                    if(total > maxSoFar){
                        maxSoFar = total;
                    }
                    total = 0;
                } else if(totals[i][j] != 0){
                    // Add to contiguous block
                    total += totals[i][j];
                }
            }
            if(total > maxSoFar){
                maxSoFar = total;
            }
        }
        return maxSoFar;
    }
};