class Solution {
public:
    bool repeatedSubstringPattern(string str) {
        int len = str.length();
        if(len < 1) return false;
        for(int i = 1; i <= len / 2; i++){
            if(len % i == 0 && str.substr(i) == str.substr(0, len-1)){
                return true;
            }
        }
        return false;
    }
};