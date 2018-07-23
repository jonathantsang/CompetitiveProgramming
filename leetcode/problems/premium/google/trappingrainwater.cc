class Solution {
    vector<int> seen;
public:
    int trap(vector<int>& height) {
        if(height.size() == 0){
            return 0;
        }
        int total = 0;
        int maximum = 0;
        int mIndex = 0;
        for(int i = 0; i < height.size(); i++){
            if(height[i] >= maximum){
                maximum = height[i];
                mIndex = i;
            }
        }
        // left
        int lmax = 0;
        for(int i = 0; i < mIndex; i++){
            if(height[i] > lmax){
                lmax = height[i];
            } else {
                total += lmax - height[i];
            }
        }
        
        // right
        int rmax = 0;
        for(int i = height.size()-1; i > mIndex; i--){
            if(height[i] > rmax){
                rmax = height[i];
            } else {
                total += rmax - height[i];
            }
        }
        return total;
    }
};