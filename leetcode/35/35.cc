class Solution {
    int binsearch(vector<int>&nums, int target, int start, int end){
        if(start >= end){
            return start;
        }
        int mid = (start + end) / 2;
        if(nums[mid] == target){
            return mid;
        } else if (nums[mid] > target) {
            return binsearch(nums, target, start, mid);
        } else {
            return binsearch(nums, target, mid+1, end);
        }
    }
public:
    int searchInsert(vector<int>& nums, int target) {
        return binsearch(nums, target, 0, nums.size());
    }
};