class Solution {
public:
    int consecutiveNumbersSum(int N) {
        vector<int> ways(N+1, 1);
        unordered_map<int, vector<int>> sumSoFar; 
        // first is the current sum, 
        // second is value to add next to get first in consecutive sum
        
        // default
        // get 1 from 1
        // sumSoFar[1].push_back(1);
        
        // ways
        ways[0] = 1;
        
        // 1 to N
        for(int i = 1; i <= N; i++){
            // check sumSoFar
            int numWays = 1;
            
            if(sumSoFar.count(i) == 0){
                // none can be formed, just one
            } else {
                // some pairs
                numWays += sumSoFar[i].size();
                for(int j = 0; j < sumSoFar[i].size(); j++){
                    // for each pair, form next ones
                    sumSoFar[i + (sumSoFar[i][j] + 1)].push_back(sumSoFar[i][j] + 1);
                }
            }
            
            ways[i] = numWays;
            // cout << i << " has " << numWays << " ways " << endl;
            sumSoFar[i+(i+1)].push_back(i+1);
            
        }
        return ways[N];
    }
};