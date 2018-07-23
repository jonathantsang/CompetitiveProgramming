class Solution {
public:
    int repeatedStringMatch(string A, string B) {
        string full = A;
        int count = 1;
        while(full.length() < B.length()){
            full += A;
            count++;
        }
        // look for B in A
        if(full.find(B) != -1){
            return count;
        }
        // check if one more makes it work
        full += A;
        count++;
        if(full.find(B) != -1){
            return count;
        }
        // else not possible
        return -1;
    }
};