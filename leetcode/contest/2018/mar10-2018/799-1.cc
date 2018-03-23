class Solution {
    void print(vector<vector<int>> d){
        for(vector<int> v : d){
            for(int val : v){
                cout << val << " ";
            }
            cout << endl;
        }
        cout << endl;
    }
    vector<vector<int>> dp;
public:
    double champagneTower(int poured, int query_row, int query_glass) {
        dp.clear();
        dp.resize(105);
        dp[0].resize(1);
        dp[0][0] = 1;
        for(int i = 1; i <= query_row+4; i++){
            dp[i].resize(i+1);
            for(int j = 0; j < i+1; j++){
                if(j == 0 || j+1 == i+1){
                    dp[i][j] = 1;
                }
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j];
            }
        }
        // print(dp);
        int row = 0;
        int filled = 0;
        int nextrowsum = 0;
        for (int n : dp[row]){
            nextrowsum += n;
        }
        //cout << "first rowsum" << nextrowsum << endl; 
        while(filled + nextrowsum <= poured){
            row++;
            if(row >= 100){
                return 0.0;
            }
            filled += nextrowsum;
            nextrowsum = 0;
            //cout << "new filled "<< filled << endl;
            for (int n : dp[row]){
                nextrowsum += n;
            }
        }
        if(filled == poured){
            row--;
        }
        //cout << "row " << row << endl;
        //cout << "fill " << filled << endl;
        //cout << "pour " << poured << endl;
        //cout << "amt remaining" << endl;
        float amtremaining = poured - filled;
        if(amtremaining == 0){
            return 1.0;
        }
        float weight = dp[query_row][query_glass];
        float v = 0;
        float total = 0;
        for(int v : dp[query_row]){
            total += v;
        }
        float frac = amtremaining * weight / total;
        return frac;
    }
};