class Solution {
public:
    bool isMatch(string s, string p) {
        if(s == ""){
            return true;
        }
        if(p == ""){
            return false;
        }
        vector<vector<int>> dp(p.length(), vector<int>(s.length(), 0)); // 0 means match not possible, 1 means match possible
        for(int i = 0; i < p.length(); i++){
            for(int j = 0; j < s.length(); j++){
                // At this point check up, left, and diagonal to the top left
                
                if(i == 0 && j == 0){
                    // just check if the same
                    if(p[i] == s[j] || p[i] == '.'){
                        dp[i][j] = 1;
                    }
                }
                
                if(p[i] == '*'){
                    // check above by 1 and 2
                    
                    // Above
                    
                    // 1 or more from *
                    if(i-1 >= 0 && dp[i-1][j] == 1 && (p[i-1] == s[j] || p[i-1] == '.')){
                        dp[i][j] = 1;
                    }
                    
                    // 0 amount from *
                    else if (i-2 >= 0 && dp[i-2][j] == 1){
                        dp[i][j] = 1;
                    }
                    
                    // Left
                    else if(j-1 >= 0 && dp[i][j-1] == 1 && (p[i-1] == s[j] || p[i-1] == '.')){
                        dp[i][j] = 1;
                    }
                    
                    // Diagonal
                    else if(i-1 >= 0 && j-1 >= 0 && dp[i-1][j-1] == 1 && (p[i-1] == s[j] || p[i-1] == '.')){
                        dp[i][j] = 1;
                    }
                    
                    // 0 amount from *
                    else if(i-2 >= 0 && j-2 >= 0 && dp[i-2][j-2] == 1){
                        dp[i][j] = 1;
                    }
                } else {
                    // diagonal works
                    if(i-1 >= 0 && j-1 >= 0 && dp[i-1][j-1] == 1 && (p[i] == s[j] || p[i] == '.')){
                        dp[i][j] = 1;
                    }
                }
                //cout << dp[i][j] << " ";
            }
            //cout << endl;
        }
        return dp[p.size()-1][s.size()-1];
    }
};