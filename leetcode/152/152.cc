class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int s = nums[0];
        int imax = s;
        int imin = s;
        for(int i = 1; i < nums.size(); i++){
            
            if(nums[i] < 0){
                swap(imax, imin);
            }
            
            imax = max(nums[i], nums[i] * imax);
            imin = min(nums[i], nums[i] * imin);
            
            s = max(s, imax);
        }
        return s;
    }
};