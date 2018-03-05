class Solution {
public:
    int numMatchingSubseq(string S, vector<string>& words) {
        int count = 0;
        map<string, int> ht;
        for(int i = 0; i < words.size(); i++){
            // Check in S
            if(ht.find(words[i]) != ht.end()){
                count += 1;
            }
            string cons = "";
            int m = 0;
            bool t = true;
            
            for(int j = 0; j < S.length(); j++){
                if(cons == words[i]){
                    count++;
                    ht[words[i]] = 1;
                    t = false;
                    break;
                }
                if(words[i][m] == S[j]){
                    cons += words[i][m];
                    m++;
                }
            }
            ht[words[i]] = 0;
            if(t && cons == words[i]){
                count++;
                ht[words[i]] = 1;
            }
        }
        return count;
    }
};