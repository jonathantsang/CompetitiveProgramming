class Solution {
public:
    
    int calculateAverage(int i, int j, int maxI, int maxJ, vector<vector<int>>& M){
        float total = M[i][j];
        float denominator = 1;
        // Top left
        if ((i - 1 >= 0) && (j - 1 >= 0)){
            total += M[i-1][j-1];
            denominator++;
        // Top Middle
        } 
        if ((i - 1 >= 0) && (j >= 0)){
            total += M[i-1][j];
            denominator++;
        // Top Right
        } 
        if ((i - 1 >= 0) && (j + 1 < maxJ)){
            total += M[i-1][j+1];
            denominator++;
        // Same Left
        }
        if ((i >= 0) && (j - 1 >= 0)){
            total += M[i][j-1];
            denominator++;
        // Same Right
        }
        if ((i >= 0) && (j + 1 < maxJ)){
            total += M[i][j+1];
            denominator++;
        // Bottom Left
        }
        if ((i + 1 < maxI) && (j - 1 >= 0)){
            total += M[i+1][j-1];
            denominator++;
        // Bottom Middle
        }
        if ((i + 1 < maxI) && (j >= 0)){
            total += M[i+1][j];
            denominator++;
        // Bottom Right
        }
        if ((i + 1 < maxI) && (j + 1 < maxJ)){
            total += M[i+1][j+1];
            denominator++;
        }
        int final = floor(total / denominator);
        return final;
    }
    
    vector<vector<int>> imageSmoother(vector<vector<int>>& M) {
        vector<vector<int>> solution;
        solution.clear();
        // Go through each cell and get the average of the surrounding cells
        int height = M.size();
        for(int i = 0; i < height; i++){
            int width = M[i].size();
            vector<int> row;
            cout << width << endl;
            for(int j = 0; j < width; j++){
                row.emplace_back(calculateAverage(i, j, height, width, M));
            }
            solution.emplace_back(row);
        }
        return solution;
    }
};