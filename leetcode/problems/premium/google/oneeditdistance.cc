class Solution {
public:
    bool isOneEditDistance(string s, string t) {
        if(s.length() == 1 + t.length()){
            // need to find if t is a substring of s with 1 missing char
            for(int i = 0; i < s.length(); i++){
                string edit = s;
                edit.erase(i, 1);
                if(t == edit){
                    return true;
                }
            }
        } else if (s.length() + 1 == t.length()){
            // need to find if s is a substring of t with 1 missing char
            for(int i = 0; i < t.length(); i++){
                string edit = t;
                edit.erase(i, 1);
                if(s == edit){
                    return true;
                }
            }
        } else if (s.length() == t.length()){
            bool lenient = true;
            // at most 1 mismatch when looking at string match
            for(int i = 0; i < s.length(); i++){
                if(s[i] == t[i]){
                    // good
                } else if (lenient){
                    // fine, one match
                    lenient = false;
                } else {
                    return false;
                }
            }
            if(lenient == true){
                return false;    
            }
            return true;
        }
        return false;
    }
};