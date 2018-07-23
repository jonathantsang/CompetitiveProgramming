class Solution {
public:
    int dominantIndex(vector<int>& nums) {
        int index = 0;
        int m = nums[0];
        for(int i = 0; i < nums.size(); i++){
            if(nums[i] > m){
                index = i;
                m = nums[i];
            }
        }
        for(int j = 0; j < nums.size(); j++){
            if(index == j){
                continue;
            }
            if(m < nums[j] * 2){
                return -1;
            }
        }
        return index;
    }
};