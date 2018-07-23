class Solution {
public:
    int numSquares(int n) {
        int d = 999999999;
        vector<int> squares;
        for(int i = 0; i < 100; i++){
            squares.push_back(pow(i,2));
        }
        
        vector<int> dp(n+1, d);
        dp[1] = 1;
        // coin change
        for(int i = 2; i <= n; i++){
            // for each coin that applies
            for(int j = 0; j < squares.size(); j++){
                if(squares[j] > i){
                    break;
                }
                // check if the coin works
                if(squares[j] == i){
                    dp[i] = 1;
                } else if(i - squares[j] > 0) {
                    dp[i] = min(dp[i], dp[i - squares[j]] + 1);
                }
            }
            // cout << dp[i] << endl;
        }
        return dp[n];
    }
};