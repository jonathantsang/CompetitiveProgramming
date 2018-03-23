class Solution {
    string shift(string s, int i){
        return s.substr(i) + s.substr(0,i);
    }
public:
    bool rotateString(string A, string B) {
        for(int i = 1; i < A.length(); i++){
            string s = shift(A, i);
            // cout << s << endl;
            if(s == B){
                return true;
            }
        }
        return false;
    }
};