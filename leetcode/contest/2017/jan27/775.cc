class Solution {
public:
    bool isIdealPermutation(vector<int>& A) {
        int global = 0;
        int local = 0;
        int maxseen = A[0];
        for(int i = 0; i < A.size(); i++){
            // check local
            if(i+1 == A.size()){
                break;
            }
            if(A[i] > A[i+1]){
                local++;
            }
            // global+1, but not local
            if(A[i+1] < maxseen && A[i] != maxseen){
                return false;
            }
            if(A[i] > maxseen){
                maxseen = A[i];
            }
            // check global
        }
        
        return true;
    }
};