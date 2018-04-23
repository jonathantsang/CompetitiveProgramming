class Solution {
public:
    int kthGrammar(int N, int K) {
        bool zero = true;
        int counter = 1;
        if(K == 1){
            return 0;
        } else if (K == 2){
            return 1;
        }
        // Count up by power of 2
        while(counter <= K){
            counter *= 2;
            zero = !zero;
        }
        if(zero){
            return 0;
        } else {
            return 1;
        } 
    }
};
