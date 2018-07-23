class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if(matrix.size() == 0){
            return false;
        }
        int y = 0;
        int x = matrix[0].size()-1;
        while(y < matrix.size() && x >= 0){
            if(matrix[y][x] == target){
                return true;
            } else if (matrix[y][x] > target){
                x--;
            } else {
                y++;
            }
        }
        return false;
    }
};