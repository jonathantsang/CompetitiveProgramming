class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        vector<int> ans;
        for(int i = 0; i < digits.size(); i++){
            ans.push_back(digits[i]);
        }
        // add to the end
        int index = digits.size()-1;
        ans[index]++;
        while(ans[index] > 9){
            // set current to 0
            ans[index] = 0;
            // meaning it is appending to the number column
            if(index <= 0){
                ans.insert(ans.begin(), 1);
                break;
            }
            // set left one add 1
            ans[index-1]++;
            index--;
        }
        return ans;
    }
};