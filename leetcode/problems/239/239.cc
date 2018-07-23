class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> arr;
        vector<int> soln;
        
        if(nums.empty()){
            return soln;
        }
        
        int i = 0;
        for(; i < k; i++){
            while(!arr.empty() && nums[i] >= nums[arr.back()]){
                arr.pop_back();
            }
            arr.push_back(i); 
        }
        
        // then for the rest of the array
        for(; i < nums.size(); i++){
            soln.push_back(nums[arr.front()]);
        
            // remove not in window
            while(!arr.empty() && arr.front() <= i - k){
                arr.erase(arr.begin());
            }
            
            // lower removed
            while(!arr.empty() && nums[i] >= nums[arr.back()]){
                arr.pop_back();
            }
            
            arr.push_back(i);
        }
        
        soln.push_back(nums[arr.front()]);
        return soln;
    }
};