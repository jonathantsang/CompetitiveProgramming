class Solution {
    map<int, vector<pair<int,int>>> log;
    map<int, int> seen; // Key is cur, val is amt so far
    // Min dist
    int dfs(int cur, int dst, int K, int amt, int steps, int keepmin){
        if(cur == dst){
            return amt;
        } else if (steps > K){
            return INT_MAX;
        }
        if(seen.find(cur) != seen.end()){
            if(seen[cur] < amt){
                return INT_MAX; // already faster path 
            }
        } else {
            seen[cur] = amt; // Got to cur with amt
        }
        
        // Each possible pathway out
        int minsofar = INT_MAX;
        for(int i = 0; i < log[cur].size(); i++){
            //cout << cur << " goes trip " << i << endl;
            int price = amt + log[cur][i].second;
            if(price > keepmin){
                continue; // Skip since it is probably inefficient
            }
            //cout << "total price " << price << endl; 
            minsofar = min(minsofar, dfs(log[cur][i].first, dst, K, price, steps+1, minsofar));
            //cout << "minsofar" << minsofar << endl;
        }
        return minsofar;
    }
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int K) {
        log.clear();
        seen.clear();
        for(int i = 0; i < flights.size(); i++){
            pair<int, int> sd; // Location [0] and Price [1]
            sd.first = flights[i][1];
            sd.second = flights[i][2];
            //cout << "log " << flights[i][0] << " having " << sd.first << " " << sd.second << endl;
            log[flights[i][0]].push_back(sd);
        }
        
        seen[src] = 0; // 0 cost start
        int val = dfs(src, dst, K, 0, 0, INT_MAX);
        if(val == INT_MAX){
            return -1;
        }
        return val;
    }
};