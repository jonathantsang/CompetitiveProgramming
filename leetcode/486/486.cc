class Solution {
    void print(vector<vector<int>> v){
        for(vector<int> row : v){
            for(int val : row){
                cout << val << " ";
            }
            cout << endl;
        }
        cout << endl;
    }
public:
    bool PredictTheWinner(vector<int>& nums) {
        vector<vector<int>> dp;
        dp.resize(nums.size());
        for(int i = 0; i < nums.size(); i++){
            dp[i].resize(nums.size());
        }
        // Want the maximum for player 1 more than half
        int allval = 0;
        for(int n : nums){
            allval += n;
        }
        // i is for end and j is for start <- v direction
        for(int i = 0; i < nums.size(); i++){
            int total = 0;
            for(int j = nums.size() - 1; j >= 0; j--){
                if(j > i)
                    continue;
                total += nums[j];
                if(j == i){
                    dp[i][j] = nums[i];
                }
                else if((i - j) == 1){
                    dp[i][j] = max(nums[i], nums[j]);
                }
                else {
                    dp[i][j] = max(total - dp[i-1][j], total - dp[i][j+1]);
                }
            }
            // print(dp);
        }
        return dp[nums.size()-1][0] >= ceil((float)allval / (float)2);
    }
};