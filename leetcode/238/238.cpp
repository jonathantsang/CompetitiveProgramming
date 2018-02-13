#include <vector>
using namespace std;

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int leng = nums.size();
        int l = 1;
        vector<int> newv;
        for(int i = 1; i < leng; i++){
            newv[i] = l;
            l *= nums[i];
        }
        int i = leng - 1;
        l = 1;
        while(i >= 0){
            newv[i] *= l;
            l *= nums[i];
            i -= 1;
        }
        return newv;
    }
};