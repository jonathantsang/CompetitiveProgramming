class Solution {
public:
    bool splitArraySameAverage(vector<int>& A) {
        int B = 0;
        int C = 0;
        for(int i = A.size(); i >= 0; i--){
            if(B == 0){
                B += A[i];
            } else if(C == 0){
                C += A[i];
            } else {
                // One is smaller, add the value to it
                if(B < C){
                    B += A[i];    
                } else {
                    C += A[i];
                }
            }
        }
        return B == C;
    }
};