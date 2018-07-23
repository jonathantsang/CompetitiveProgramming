class Solution {
    bool checkPeak(vector<int> &A, int idx){
        // left
        for(int i = 1; i <= idx; i++){
            if(A[i] < A[i-1]){
                return false;
            }
        }
        for(int i = idx; i < A.size(); i++){
            if(A[i] < A[i+1]){
                return false;
            }
        }
        return true;
    }
public:
    int peakIndexInMountainArray(vector<int>& A) {
        for(int i = 0; i < A.size(); i++){
            if(checkPeak(A, i)){
                return i;
            }
        }
        return -1; // none but should have one
    }
};