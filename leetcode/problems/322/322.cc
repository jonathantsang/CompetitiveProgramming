class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<int> dp;
        map<int, int> coin;
        int mc = 0;
        dp.resize(200);
        for(int i = 0; i < coins.size(); i++){
            coin[coins[i]] = 1;
            mc = max(mc, coins[i]);
        }
        dp.resize(mc);
        dp[1] = INT_MAX;
        int a = 0;
        for(int j = 1; j <= amount; j++){
            for(int i = 0; i < coins.size(); i++){
                // Exact coin
                if(coins[i] == j){
                    dp[j] = 1;
                } else if (coins[i] < j){
                    cout << j << "da " << endl;
                // Make the change
                    a = 1 + dp[j - coins[i]];
                    if(a < dp[j]){
                        dp[j] = a;
                    }
                }
            }
            cout << j << " " << dp[j] << endl;
        }
        if(dp[amount] == 0){
            return -1;
        }
        return dp[amount];
    }
};