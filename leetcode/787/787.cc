class Solution {
    void print(vector<vector<int>> d){
        for(auto r : d){
            for(auto v : r){
                cout << v << " ";
            }
            cout << endl;
        }
        cout << endl;
    }
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int K) {
        vector<vector<int>> dp; // [to what node][num steps]
        dp.resize(n);
        K++;
        for(int i = 0; i < n; i++){
            dp[i].resize(K+1);
            fill(dp[i].begin(), dp[i].end(), 100001);
        }
        dp[src][0] = 0;
        print(dp);
        // For each city
        for(int i = 1; i <= K; i++)
        {
            for(int j = 0; j < n; j++)   //To update dp[j][i](using i steps), we copy dp[j][i-1] first
                dp[j][i] = dp[j][i-1];
            for(const vector<int>& f: flights)
            {
                dp[f[1]][i] = min(dp[f[1]][i], dp[f[0]][i-1] + f[2]);
            }
            print(dp);
        }
        if(dp[dst][K] == 10001){
            return -1;
        }
        return dp[dst][K];
    }
};