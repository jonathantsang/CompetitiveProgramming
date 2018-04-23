class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int i = 1;
        while(i < nums.size()){
            if(nums[i-1] == nums[i]){
                nums.erase(nums.begin()+i-1);
            } else {
                i++;
            }
        }
        return nums.size();;
    }
};