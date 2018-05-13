class Solution {
public:
    int consecutiveNumbersSum(int N) {
        vector<int> ways(N+1, 1);
        vector<pair<int, int>> sumSoFar; // first is the current sum, second is the next value to add
        
        // default
        pair<int, int> p;
        p.first = 0;
        p.second = 1;
        sumSoFar.push_back(p);
        
        // ways
        ways[0] = 1;
        
        // 1 to N
        for(int i = 1; i <= N; i++){
            // Each of sumSoFar
            int numWays = 1;
            for(int j = 1; j < sumSoFar.size(); j++){
                // check if adding the next value would make it larger
                if(sumSoFar[j].first + sumSoFar[j].second == i){
                    numWays++;
                    sumSoFar[j].first += sumSoFar[j].second;
                    sumSoFar[j].second += 1;
                }
            }
            ways[i] = numWays;
            // cout << i << " has " << numWays << " ways " << endl;
            pair<int,int> np;
            np.first = i;
            np.second = i+1;
            sumSoFar.push_back(np);
        }
        return ways[N];
    }
};