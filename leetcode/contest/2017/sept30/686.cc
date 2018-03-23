class Solution {
    bool checkSubstring(string A, string B){
        int aLeng = A.length();
        int bLeng = B.length();
        if(aLeng < bLeng){
            return false;
        }
        // Goes through each character in A
        for(int i = 0; i < aLeng; i++){
            if(A[i] == B[0]){
                // Check for the whole string of B with A
                bool substring = true;
                for(int j = 0; j < bLeng; j++){
                    if(A[i+j] != B[j]){
                        substring = false;
                        break;
                    }
                }
                if(substring == true){
                    return true;
                }
            }
        }
        return false;
    }
    
public:
    int repeatedStringMatch(string A, string B) {
        bool repeated = false;
        int repeatTimes = 1;
        int aLeng = A.length();
        int bLeng = B.length();
        string oldA = A;
        while(true){
            // Check if substring
            if(checkSubstring(A, B)){
                return repeatTimes;
            }
            
            // Check exit
            if(repeated && aLeng > bLeng){
                return -1;
            }
            
            // Not a substring
            A = A + oldA;
            repeatTimes++;
            repeated = true;
            int aLeng = A.length();
        }
        return -1;
    }
};