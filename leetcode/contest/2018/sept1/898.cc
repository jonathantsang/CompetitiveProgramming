class Solution {
public:
    int subarrayBitwiseORs(vector<int>& A) {
        set<int> possible;
        // Now recurse on possibilities
        for(int i = 0; i < A.size(); i++){
            int value = 0;
            for(int j = i; j < A.size(); j++){
                // cout << value << "OR with " << vals[j] << endl;
                value |= A[j];
                // cout << value << endl;
                if(possible.count(value) == 0){
                    // cout << value << endl;
                    possible.insert(value);
                }
            }
        }
        return possible.size();
    }
};