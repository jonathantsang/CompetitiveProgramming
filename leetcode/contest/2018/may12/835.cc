class Solution {
    int verify(vector<vector<int>>& A, int xStart, int xEnd, int yStart, int yEnd, vector<vector<int>>& B, int xOffset, int yOffset){
        int count = 0;
        for(int i = 0; i < A.size(); i++){
            for(int j = 0; j < A[i].size(); j++){
                if(i + yOffset > -1 && i + yOffset < B.size()  && j + xOffset > -1 && j + xOffset < B.size()){
                    if(A[i+yOffset][j+xOffset] == 1 && B[i][j] == 1){
                        count++;
                    }
                }
            }
        }
        return count;
    }
    
public:
    int largestOverlap(vector<vector<int>>& A, vector<vector<int>>& B) {
        int xLen = 1;
        int yLen = 1;
        int bestsofar = 0;
        vector<pair<int, int>> possible;
        // build up A
        for(int i = 0; i < A.size(); i++){
            for(int j = 0; j < A.size(); j++){
                // based on the size of A from xLen to yLen
                
                // find best pairs from defined A size at each offset
                int count = verify(A, j, j+1, i, i+1, B, 0, 0);
                
            }
        }
    }
};