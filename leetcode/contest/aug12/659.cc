class Solution {
public:
    bool isPossible(vector<int>& nums) {
        vector<vector<int>> solutions;
        
        // Try to form as many 3 consecutive as you can
        bool constructing = true;
        int leng = nums.size();
        int index = 0;
        while(index < leng){
            vector<int> subseq;
            subseq.emplace_back(nums[index]);
            nums.erase(nums.begin() + index);
            for(int i = index; i < leng; i++){
                int subleng = subseq.size();
                // If the value is 1 more
                if(nums[i] == subseq[subleng-1] + 1){
                    subseq.emplace_back(nums[index]);
                    nums.erase(nums.begin() + index);
                }
            }
            // Third value
            for(int i = index; i < leng; i++){
                int subleng = subseq.size();
                // If the value is 1 more
                if(nums[i] == subseq[subleng-1] + 1){
                    subseq.emplace_back(nums[index]);
                    nums.erase(nums.begin() + index);
                }
            }
            int subleng = subseq.size();
            if(subleng < 3){
                // Put back values that were popped
                for(int i = 0; i < subleng; i++){
                    nums.emplace_back(subseq[i]);
                }
                break;
            } else {
                solutions.emplace_back(subseq);
            }
        }
        
        // Print
        int newleng = nums.size();
        for(int i = 0; i < newleng; i++){
            cout << nums[i] << endl;
        }
        int ss = solutions.size();
        for(int i = 0; i < ss; i++){
            int sss = solutions[i].size();
            for(int j = 0; j < sss; j++){
                cout << solutions[i][j];
            }
            cout << endl;
        }
        
        // Fill in rest of groups with remaining
        bool complete = false;
        while(!complete){
            complete = true;
        }
        return true;
    }
};