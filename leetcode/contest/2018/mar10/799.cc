class Solution {
    vector<vector<int>> dp;
public:
    double champagneTower(int poured, int query_row, int query_glass) {
        dp.clear();
        dp.resize(101);
        for(int i = 0; i < 101; i++){
            dp[i].resize(i+1);
        }
        int filled = 0;
        int row = 0;
        int increment = 1;
        for(j = 0; j < 101; j++){
            for(int i = 0; i < increment; i++){
                if(i - 1 < 0 || i + 1 == increment){
                    dp[row][i] = 1;
                } else {
                    dp[row][i] = dp[row-1][i-1] + dp[row-1][i];
                }
                // cout << dp[row][i] << endl;
            }
        }
        if(poured == 0){
            return 0.0;
        }
        dp[0][0] = 1;
        // cout << "test " << endl;
        while(filled + increment <= poured){
            filled += increment;
            row++;
            if(row >= 100){
                return 1.0; // Has to be full
            }
            for(int i = 0; i < dp[row].size(); i++){
                increment += dp[row][i];
            }
            // cout << row << endl;
            // Sum two previous above
            
        }
        // cout << "survived" << endl;
        if(filled == poured){
            row--;
        }
        // Row is last filled up row
        cout << row << endl;
        // Row less than query
        if(row > query_row){
            return 1.0;
        } else if (row < query_row){
            return 0.0;
        }
        
        float amtleft = (float) (poured - filled);
        float portion = 0;
        float total = 0;
        for(int i = 0; i < dp[query_row].size(); i++){
            total += dp[query_row][i];
            if(i == query_glass){
                portion = dp[query_row][i];
            }
        }
        if(portion == 0){
            portion = 1;
        }
        cout << portion << endl;
        cout << "t " << total << endl;
        portion /= total; // fractional of whole thing
        float frac =  amtleft * portion;
        return frac;
    }
};