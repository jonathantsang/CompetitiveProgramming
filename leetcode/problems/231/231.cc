class Solution {
public:
    bool isPowerOfTwo(int n) {
        // binary
        if(n <= 0){
            return false;
        }
        int i = 0;
        bool fine = true;
        while(n >> i > 0){
            if(((n >> i) & 1) == 1){
                if(fine){
                    fine = false;
                } else {
                    return false;
                }
            }
            i++;
        }
        return true;
    }
};