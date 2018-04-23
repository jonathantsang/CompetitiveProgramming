class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        int leng = nums.size();
        vector<int> dupes;
        int last = 1;
        for(int i = 0; i < leng; i++){
            // length test
            if(abs(nums[i]) == leng){
                if(last < 0){
                    dupes.push_back(leng);
                } else {
                    last = -last;
                }
            } else if(nums[abs(nums[i])] < 0){
                dupes.push_back(abs(nums[i]));
            } else {
                nums[abs(nums[i])] = -nums[abs(nums[i])];
            }
        }
        return dupes;
    }
};