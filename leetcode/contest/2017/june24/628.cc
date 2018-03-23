class Solution {
public:
    int maximumProduct(vector<int>& nums) {
        int total = 0;
        int maxi = -1000;
        int m1;
        if(nums.size() == 0)
            return 0;
        for(int i = 0; i < nums.size(); i++){
            if(nums[i] > maxi){
                maxi = nums[i];
                m1 = i;
            }
        }
        cout << maxi << endl;
        // maxi is set as maximum value
        // Check either two negative are max, or two positive
        int bestnegative = 0;
        int bestpositive = 0;
        int pos1 = -1001;
        int pos2 = -1001;
        int neg1 = 1001;
        int neg2 = 1001;
        // Look for best positive and second best after maxi
        for(int i = 0; i < nums.size(); i++){
            if(nums[i] > pos2 && i != m1){
                if(nums[i] > pos1){
                    pos2 = pos1;
                    pos1 = nums[i];
                } else {
                    pos2 = nums[i];
                }
            }
        }
        bestpositive = pos1 * pos2 * maxi;
        for(int i = 0; i < nums.size(); i++){
            if(nums[i] < neg2){
                if(nums[i] < neg1){
                    neg2 = neg1;
                    neg1 = nums[i];
                } else {
                    neg2 = nums[i];
                }
            }
        }
        bestnegative = neg1 * neg2 * maxi;
        return max(bestnegative, bestpositive);
    }
};