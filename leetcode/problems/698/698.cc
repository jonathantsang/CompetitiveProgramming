class Solution {    
    bool recurse(vector<int>& nums, int subsum, vector<int> sums, int val, int j){
        // cout << sums[0] << "," << sums[1] << "," << sums[2] << " index " << j << endl;
        bool result = false;
        // For each possible array it can go into
        for(int i = 0; i < sums.size(); i++){            
            // Can go to that sums[i] subset
            if(sums[i] + val <= subsum){
                if(j+1 == nums.size()){
                    return true;
                }
                sums[i] += val;
                result = recurse(nums, subsum, sums, nums[j+1], j+1);
                // After lower recursion is returned
                if(result == false){
                    // Reset the sums
                    sums[i] -= val;
                    // cout << "fail" << endl;
                }
                if(result == true){
                    return true;
                }
            }
            if(sums[i] == 0){
                break;
            }
            
        }
        return result;
    }
public:
    bool canPartitionKSubsets(vector<int>& nums, int k) {
        int total = 0;
        for(vector<int>::iterator it = nums.begin(); it != nums.end(); it++){
            total += *it;
        }
        int subsum = total / k;
        if(total % k != 0){
            return false;
        }
        vector<int> sums;
        sums.resize(k);
        bool result = recurse(nums, subsum, sums, nums[0], 0); // next value joins
        return result;
    }
};