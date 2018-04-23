class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        vector<vector<int>> sums;
        // Go through rows and get minimum sums
        for(int i = 1; i < triangle.size(); i++){
            for(int j = 0; j < triangle[i].size(); j++){
                // First and last
                if(j == 0){
                    triangle[i][j] += triangle[i-1][j];
                } else if(j + 1 == triangle[i].size()){
                    triangle[i][j] += triangle[i-1][j-1]; // j-1 last row is one shorter
                } else {
                   triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j]); 
                }
            }
        }
        int minval = INT_MAX;
        for(int i = 0; i < triangle[triangle.size()-1].size(); i++){
            minval = min(triangle[triangle.size()-1][i], minval);
        }
        return minval;
    }
};