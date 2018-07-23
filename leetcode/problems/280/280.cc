class Solution {
public:
    void wiggleSort(vector<int>& nums) {
        if(nums.size() == 0){
            return;
        }
        if(nums.size() == 1){
            return;
        }
        for(int i = 0; i < nums.size()-1; i++){
            if(i % 2 == 0){
                // even
                // want num[i] <= num[i+1]
                if(nums[i] > nums[i+1]){
                    // swap
                    int temp = nums[i];
                    nums[i] = nums[i+1];
                    nums[i+1] = temp;
                }
            } else {
                // odd
                // want num[i] >= num[i+1]
                if(nums[i] < nums[i+1]){
                    // swap
                    int temp = nums[i];
                    nums[i] = nums[i+1];
                    nums[i+1] = temp;
                }
            }
        }
    }
};