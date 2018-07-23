class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        int perimeter = 0;
        for(int i = 0; i < grid.size(); i++){
            for(int j = 0; j < grid[i].size(); j++){
                // grid[i][j]
                if(grid[i][j] == 1){
                    // check if it has a 1 to the top or to the left
                    int newEdges = 4;
                    if(i-1 >= 0 && grid[i-1][j] == 1){
                        newEdges -= 2;
                    }
                    if(j-1 >= 0 && grid[i][j-1] == 1){
                        newEdges -= 2;
                    }
                    perimeter += newEdges;
                }
            }
        }
        return perimeter;
    }
};