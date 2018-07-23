class Solution {
public:
    int numDecodings(string s) {
        map<int, int> costs;
        for(int i = 1; i < 27; i++){
            costs[i] = 1; // valid decode
        }
        vector<int> ways(s.length()+1);
        ways[0] = s[0] == '0' ? 0 : 1;
        if(ways[0] == 0){
            return 0;
        }
        
        for(int i = 1; i < s.length(); i++){
            int countways = 0;
            
            // one digit addition to dp always
            int one = stoi(s.substr(i,1));
            int two = stoi(s.substr(i-1,2));
            //cout << "ot " << one << " " << two << endl;
            if(costs.count(one) > 0){
                countways = ways[i-1];
            } else if (costs.count(two) > 0){
                // has to be 0 since it failed one
                if(i == 1){
                    // has at least one since it is two and it is in costs
                    countways += 1;
                } else {
                    countways += ways[i-2];
                }
                
            }

            // two digit addition to dp, no leading 0s
            if(one != 0){
                if(two > 9 && costs.count(two) > 0){
                    // it is in it
                    if(i == 1){
                        // has at least one since it is two and it is in costs
                        countways += 1;
                    } else {
                        countways += ways[i-2];
                    }
                }
            }
            
            
            
            //cout << i << " " << countways << endl;
            ways[i] = countways;
        }
        return ways[s.length()-1];
    }
};