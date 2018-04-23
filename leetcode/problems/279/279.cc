class Solution {
public:
    int numSquares(int n) {
        vector<int> dp;
        dp.resize(n+1);
        fill(dp.begin(), dp.end(), 0);
        for(int i = 1; i <= n; i++){
            int val = INT_MAX;
            // Go through perfect squares up to i
            for(int j = 1; j <= i; j++){
                if(j * j <= i){
                    val = min(val, dp[i- j*j] + 1);
                }
            }
            dp[i] = val;
        }
        return dp[n];
    }
};