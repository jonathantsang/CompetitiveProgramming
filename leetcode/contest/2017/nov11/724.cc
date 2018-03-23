class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int left = 0;
        int right = 0;
        int leng = nums.size();
        for(int i = 0; i < leng; i++){
            total += nums[i];
        }
        right = total;
        for(int i = 0; i < leng; i++){
            right -= nums[i];
            if(left == right){
                return i;
            }
            left += nums[i];
        }
        return -1;
    }
};