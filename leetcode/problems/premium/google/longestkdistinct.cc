class Solution {
public:
    int lengthOfLongestSubstringKDistinct(string s, int k) {
        if(s.length() <= k){
            return s.length();
        }
        if(k == 0){
            return 0;
        }
        vector<int> last_seen(256, -1);
        int maxlen = 0;
        int start = 0;
        int end = 0;
        int count = 0;
        while(end < s.length()){
            // cout << start << " " << end << endl;
            if(count < k || start <= last_seen[s[end]]){
                maxlen = max(maxlen, end - start+1);
                if(last_seen[s[end]] < start) count++;
                
                last_seen[s[end]] = end;
                
                end++;
            } else {
                if(last_seen[s[start]] == start) count--;
                start++;
            }
        }
        return maxlen;
    }
};