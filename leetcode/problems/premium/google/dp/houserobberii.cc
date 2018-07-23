class Solution {
public:
    int rob(vector<int>& nums) {
        if(nums.size() == 0){
            return 0;
        } else if (nums.size() == 1){
            return nums[0];
        } else if (nums.size() == 2){
            return max(nums[0], nums[1]);
        }
        
        int m = 0;
        vector<int> dp(nums.size(), 0);
        dp[0] = nums[0];
        dp[1] = max(nums[0], nums[1]);
        
        // do it for 0 to n-2
        for(int i = 2; i < nums.size() - 1; i++){
            dp[i] = max(dp[i-1], dp[i-2] + nums[i]);
        }
        
        m = dp[nums.size()-2]; // max up to here
        // cout << "m is " << m << endl;
        
        fill(dp.begin(), dp.end(), 0);
        dp[0] = 0;
        dp[1] = nums[1];
        
        // do it for 1 to n-1
        for(int i = 2; i < nums.size(); i++){
            dp[i] = max(dp[i-1], dp[i-2] + nums[i]);
        }
        
        m = max(m, dp[nums.size()-1]);
        return m;
    }
};