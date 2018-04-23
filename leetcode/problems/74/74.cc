class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int i = 0;
        if(matrix.size() == 0){
            return false;
        }
        int j = matrix[0].size()-1;
        if(j < 0){
            return false;
        }
        while(i < matrix.size() && j >= 0){
            if(matrix[i][j] == target){
                return true;
            } else if (matrix[i][j] > target){
                j--;
            } else if (matrix[i][j] < target){
                i++;
            }
        }
        return false;
    }
};