class Solution {
public:
    bool backspaceCompare(string S, string T) {
        int len = S.length();
        for(int i = 0; i < len; i++){
            if(S[i] == '#'){
                if(i == 0){
                    S.erase(0,1);
                    i -= 1;
                } else {
                    S.erase(i-1, 2);
                    i-=2;
                }
            }
            len = S.length();
        }
        len = T.length();
        // T
        for(int i = 0; i < len; i++){
            // cout << i << endl;
            if(T[i] == '#'){
                if(i == 0){
                    T.erase(0,1);
                    i -=1;
                } else {
                    T.erase(i-1, 2);
                    i -= 2;
                }
            }
            // cout << T << endl;
            len = T.length();
        }
        // cout << S << " " << T << endl;
        return S == T;
    }
};