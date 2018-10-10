class Solution {
public:
    string decodeAtIndex(string S, int K) {
        string cur;
        string store = cur;
        int idx = 0;
        map<int, string> range_query; // At the higher end, store the string ex. 3 has leet
        for(int i = 0; i < S.length(); i++){
            if(isdigit(S[i])){
                // Cut off the word here
                if(cur == ""){
                    cur = store;
                }
                range_query[idx] = cur;
                
                // Then also do it for the repeat digits
                int times = S[i] - '0';
                int update = cur.length() * (times-1);
                idx += update;
                // Past strings as well
               
                // Just passed it in repeat
                if(idx >= K){
                    int lookingfor = K - idx;
                    // Now search the original range for that index, and go deeper if necessary
                    while(true){
                        for(pair<int, string> p : range_query){
                            // Check if in range with valid string
                            if(p.first > lookingfor && p.second != "REPEAT_STOP_HARDCODE"){
                                int low = (*range_query.lower_bound(lookingfor)).first;
                                int charIndex = lookingfor - low;
                                string s(1, p.second[charIndex]);
                                return s;
                            }
                            
                            // First bigger, in range
                            else if(p.first > lookingfor){
                                lookingfor = p.first - lookingfor;
                                // Use looking for from the front of this segment now
                                break;
                            }
                        }
                    }
                }
                // Update to know this is a "repeat stop"
                range_query[idx] = "REPEAT_STOP_HARDCODE";
                cur = "";
                
            } else {
                // character
                if(cur == "" && store != ""){
                    store = "";
                }
                
                if(idx == K){
                    // Do the business
                    string s(1, S[i]);
                    return s;
                }
                cur += S[i];
            }
            idx++;
        }
        return "a";
    }
};