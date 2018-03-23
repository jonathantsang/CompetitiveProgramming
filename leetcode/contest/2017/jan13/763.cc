class Solution {
    map<char, int> min;
    map<char, int> max;
public:
    vector<int> partitionLabels(string S) {
        // Go through each character of the label
        for(int i = 0; i < S.length(); i++){
            if(min.find(S[i]) != min.end()){
                max[S[i]] = i;
            } else {
                min[S[i]] = i;
                max[S[i]] = i;
            }
        }
        
        // See maps
        /*
        cout << "min" << endl;
        for(map<char,int>::iterator it = min.begin(); it != min.end(); ++it) {
            cout << it->first << " " << it->second << endl;
        }
        cout << "max" << endl;
        for(map<char,int>::iterator it = max.begin(); it != max.end(); ++it) {
            cout << it->first << " " << it->second << endl;
        }*/
        
        // Go and make the partition
        vector<int> result;
        int currmin = min[0];
        int currmax = max[0];
        map<char, int> met;
        
        for(int i = 0; i < S.length(); i++){
            // S[i] char
            if(met.find(S[i]) != met.end()){
                continue;
            } else {
                met[S[i]] = 1;
            }
            
            // Go through until the character period is outside of the currmax
            if(max[S[i]] <= currmax && min[S[i]] >= currmin){
                // fine
                
            // In this case expand the max because it is in the range, but larger max
            } else if (max[S[i]] >= currmax && min[S[i]] >= currmin && min[S[i]] <= currmax){
                currmax = max[S[i]];
                
            // In this case it is outside of the range, so calculate the total
            } else if (max[S[i]] > currmax && min[S[i]] > currmin && min[S[i]] > currmax){
                int length = currmax - currmin + 1;
                result.emplace_back(length);
                
                // Reset to new value
                currmin = min[S[i]];
                currmax = max[S[i]];
            }
        }
        // Last one
        int length = currmax - currmin + 1;
        result.emplace_back(length);
        
        return result;
    }
};