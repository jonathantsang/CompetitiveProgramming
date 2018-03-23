class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        double maximum = -10000;
        int leng = nums.size();
        double p = k;
        double base = 0;
        // Base average
        for(int j = 0; j < k; j++){
            base += nums[j];
        }
        maximum = base / p;
        for(int i = 1; i + k <= leng; i++){
            base -= nums[i-1];
            base += nums[(i-1)+k];
            double calc = base / p;
            if(calc > maximum){
                maximum = calc;
            }
        }
        return maximum;
    }
};