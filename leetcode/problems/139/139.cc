class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        vector<bool> dp;
        dp.resize(s.length());
        string part = "";
        unordered_set<string> d;
        for(auto s : wordDict){
            d.insert(s);
        }
        for(int i = 0; i < s.length(); i++){
            part += s[i];
            if(d.find(part) != d.end()){
                part = "";
                dp[i] = true; 
            }
        }
        return dp[s.length()-1];
    }
};