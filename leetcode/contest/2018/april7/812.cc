class Solution {
    double area(int x1, int y1, int x2, int y2, int x3, int y3){
        return abs(0.5*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)));
    }
public:
    double largestTriangleArea(vector<vector<int>>& points) {
        double maxArea = 0;
        // For each point
        for(int i = 0; i < points.size(); i++){
            for(int j = 0; j < points.size(); j++){
                if(j == i){
                    continue;
                }
                for(int k = 0; k < points.size(); k++){
                    if(k == i || k == j){
                        continue;
                    }
                    // Check the other two possible points
                    maxArea = max(maxArea, area(points[i][0], points[i][1], points[j][0], points[j][1], points[k][0], points[k][1]));
                }
            }
        }
        return maxArea;
    }
};