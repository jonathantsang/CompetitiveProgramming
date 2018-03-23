class Solution {
public:
    int numJewelsInStones(string J, string S) {
        map<char, int> ht;
        int count = 0;
        for(int i = 0; i < J.size(); i++){
            if(ht.find(J[i]) == ht.end()){
                ht[J[i]] = 1;
            } else {
                ht[J[i]] += 1;
            }
        }
        for(int i = 0; i < S.size(); i++){
            if(ht.find(S[i]) != ht.end()){
                count++;
            }
        }
        return count;
    }
};