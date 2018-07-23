class Solution {
    int lastR = 0;
    int findMountainLength(vector<int> &A, int index){
        int leng = 0;
        int left = 0;
        int right = 0;
        bool leftend = false;
        bool rightend = false;
        // left
        for(int i = index-1; i >= 0; i--){
            if(A[i] < A[i+1]){
                // good
                leftend = true;
            } else {
                left = i;
                leftend = false;
                break;
            }
        }
        
        if(leftend == true){
            left = -1;
        }
        
        // right
        for(int i = index+1; i < A.size(); i++){
            if(A[i] < A[i-1]){
                // good
                rightend = true;
            } else {
                right = i;
                lastR = i;
                rightend = false;
                break;
            }
        }
        
        if(rightend == true){
            right = A.size();
            lastR = A.size();
        }
        
        // cout << left << " " << right << endl;
        
        leng = 1 + (index - left - 1) + (right - index - 1);
        // cout << lastR << endl;
        return leng;
    }
public:
    int longestMountain(vector<int>& A) {
        if(A.size() <= 2){
            return 0;
        }
        int bestMountain = 0;
        for(int i = 1; i < A.size()-1; i++){
            if(A[i] > A[i-1] && A[i] > A[i+1]){
                bestMountain = max(bestMountain, findMountainLength(A, i));
                i = lastR; // set to after mountain possible
                i--; // try to maintain i to lastR
            }
        }
        return bestMountain;
    }
};