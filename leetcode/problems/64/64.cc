class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        vector<vector<int>> dp = grid;
        for(int i = 1; i < grid.size(); i++){
            fill(dp[i].begin()+1, dp[i].end(), 0); 
        }
        for(int i = 0; i < grid.size(); i++){
            for(int j = 0; j < grid[i].size(); j++){
                if(i == 0 && j == 0){
                    dp[0][0] = grid[0][0];
                }
                // Find min between top or left value for each value in the row
                else if(i-1 < 0){
                    dp[i][j] = dp[i][j-1] + grid[i][j];
                }
                else if(j-1 < 0){
                    dp[i][j] = dp[i-1][j] + grid[i][j];
                } else {
                    dp[i][j] = min(dp[i-1][j] + grid[i][j], dp[i][j-1] + grid[i][j]); 
                }
            }
        }
        return dp[grid.size()-1][grid[0].size()-1];
    }
};