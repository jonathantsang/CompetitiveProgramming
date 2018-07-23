class Solution {
public:
    vector<vector<int>> transpose(vector<vector<int>>& A) {
        vector<vector<int>> transpose;
        // each column
        for(int i = 0; i < A[0].size(); i++){
            // each row
            vector<int> row;
            for(int j = 0; j < A.size(); j++){
                row.push_back(A[j][i]);
                // cout << A[j][i] << endl;
            }
            transpose.push_back(row);
        }
        return transpose;
    }
};