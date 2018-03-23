class Solution {
public:
    bool hasAlternatingBits(int n) {
        int previous = n & 1;
        n >>= 1;
        while (n != 0) {
            if((n & 1) == previous){
                return false;
            }
            previous = n & 1;
            n >>= 1;
        }
        return true;
    }
};