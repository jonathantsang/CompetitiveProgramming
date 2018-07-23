class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        vector<int> row(grid[0].size(), INT_MAX);
        vector<vector<int>> costs(grid.size(), row);
        for(int i = 0; i < grid.size(); i++){
            for(int j = 0; j < grid[0].size(); j++){
                if(i-1 >= 0){
                    costs[i][j] = min(costs[i][j], costs[i-1][j] + grid[i][j]);
                }
                if(j-1 >= 0){
                    costs[i][j] = min(costs[i][j], costs[i][j-1] + grid[i][j]);
                }
                if(i-1 < 0 && j-1 < 0){
                    costs[i][j] = grid[i][j];
                }
                // cout << costs[i][j] << endl;
            }
        }
        return costs[grid.size()-1][grid[0].size()-1];
    }
};