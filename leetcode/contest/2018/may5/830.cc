class Solution {
public:
    vector<vector<int>> largeGroupPositions(string S) {
        vector<vector<int>> groups;
        int start = 0;
        int end = 0;
        char c = S[0];
        for(int i = 1; i < S.length(); i++){
            if(c == S[i]){
                // continue group
                end = i;
            } else {
                // break group
                
                // large?
                if((end - start) >= 2){
                    vector<int> pair;
                    pair.push_back(start);
                    pair.push_back(end);
                    groups.push_back(pair);
                }
                  
                start = i;
                end = i;
                c = S[i];
            }
        }
        return groups;
    }
};