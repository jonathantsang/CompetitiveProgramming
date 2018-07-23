class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int maxlen = 0;
        vector<int> dp(nums.size(), 0);
        dp[0] = nums[0] == 1 ? 1 : 0;
        maxlen = max(maxlen, dp[0]);
        for(int i = 1; i < nums.size(); i++){
            if(nums[i] == 1){
                if(nums[i-1] == 1){
                    dp[i] = dp[i-1] + 1;
                    maxlen = max(maxlen, dp[i]);
                } else {
                    dp[i] = 1;
                    maxlen = max(maxlen, dp[i]);
                }
            } else {
                dp[i] = 0;
                maxlen = max(maxlen, dp[i]);
            }
        }
        return maxlen;
    }
};