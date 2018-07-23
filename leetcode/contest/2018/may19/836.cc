class Solution {
    bool checkX(vector<int>& rec1, vector<int>& rec2){
        if(rec1[0] < rec2[0]){
            // x is less than the other
            if(rec1[2] > rec2[0]){
                return true;
            }
            return false;
        } else if (rec1[0] >= rec2[0] && rec1[2] < rec2[2]){
            // in between
            return true;
        } else {
            // greather than the other one
            if(rec2[2] > rec1[0]){
                return true;
            }
            return false;
        }
    }
    bool checkY(vector<int>& rec1, vector<int>& rec2){
        if(rec1[1] > rec2[1]){
            // y value is greater than the other square
            if(rec1[1] < rec2[3]){
                return true;
            }
            return false;
        } else if (rec1[1] >= rec2[1] && rec1[1] < rec2[3]){
            // in between
            return true;
        } else {
            // it is below
            if(rec1[3] > rec2[1]){
                return true;
            }
            return false;
        }
    }
public:
    bool isRectangleOverlap(vector<int>& rec1, vector<int>& rec2) {
        return checkX(rec1, rec2) && checkY(rec1, rec2);
    }
};