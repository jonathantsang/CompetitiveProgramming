class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        // with space
        vector<int> seen(nums.size()+1, 0);
        for(int i = 0; i < nums.size(); i++){
            seen[nums[i]] = 1;
        }
        vector<int> notIn;
        for(int i = 1; i < nums.size()+1; i++){
            if(seen[i] == 0){
                notIn.push_back(i);
            }
        }
        return notIn;
    }
};