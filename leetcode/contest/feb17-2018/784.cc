class Solution {
    vector<string> perm;
public:
    string replace(string &S, int i, char C){
        if(isupper(C)){
            S[i] = tolower(C);
        } else {
            S[i] = toupper(C);
        }
        return S;
    }
    
    void run(string S, int start){
        // Go through each char in the word
        for(int i = start+1; i < S.length(); i++){
            if((S[i] >= 'a' && S[i] <= 'z') || (S[i] >= 'A' && S[i] <= 'Z')){
                string copy = S;
                string ns = replace(copy, i, S[i]);
                perm.push_back(copy);
                run(copy, i); // Run for new list with new char
            }
        }     
    }
    
    vector<string> letterCasePermutation(string S) {
        perm.clear();
        perm.push_back(S);
        run(S);
        return perm;
    }
};