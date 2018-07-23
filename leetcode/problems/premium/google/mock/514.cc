class Solution {
public:
    int findRotateSteps(string ring, string key) {
        vector<vector<int>> dp(key.size(), vector<int>(ring.length(), -1));
        
        int cost = key.size();
        
        for(int i = 0; i < ring.size(); i++){
            if(ring[i] == key[0]){
                int a = ring.length() - i;
                dp[0][i] = min(i, a); // first 
            }
        }
        
        for(int i = 1; i < key.length(); i++){
            // go to each ring char
            for(int j = 0; j < ring.length(); j++){
                if(ring[j] == key[i]){
                    // look through the possible values for the minimum distance
                    int closest = INT_MAX;
                    for(int k = 0; k < ring.length(); k++){
                        // check if valid to go from
                        if(dp[i-1][k] > -1){
                            // clockwise vs counterclockwise
                            int way = abs(k - j);
                            int otherway = abs(ring.size() - abs(k - j));
                            int best = min(way, otherway) + dp[i-1][k];
                            closest = min(best, closest);
                        }
                    }
                    dp[i][j] = closest;
                }
                // cout << dp[i][j] << " ";
            }
            // cout << endl;
        }
        
        int steps = INT_MAX;
        // get the minimum from the last row
        for(int i = 0; i < ring.length(); i++){
            if(dp[key.size()-1][i] != -1){
                steps = min(steps, dp[key.length()-1][i]);
            }
        }
        // cout << steps << endl;
        
        return cost + steps; 
    }
};