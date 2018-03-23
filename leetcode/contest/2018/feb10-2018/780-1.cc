class Solution {
    bool check(int sx, int sy, int tx, int ty){
        // cout << tx << " " << ty << endl;
        bool c = false;
        if(tx < sx || ty < sy){
            return false;
        }
        if(sx == tx && sy == ty){
            return true;
        }
        // At one point if it is valid it needs to have that value
        if(sx == tx){
            int times = (ty - sy) / tx; // Don't go too low -sy
            ty -= tx * times;
            if(times == 0){
                return false; // Local min
            }
            c = check(sx, sy, tx, ty);
        } else if (sy == ty){
            int times = (tx - sx) / ty; // Don't go too low -sx
            tx -= ty * times;
            if(times == 0){
                return false; // Local min
            }
            c = check(sx, sy, tx, ty);
        } else if (ty > tx){
            int times = (ty - sy) / tx; // Don't go too low -sy
            ty = ty - tx * times;
            if(times == 0){
                return false; // Local min
            }
            c = check(sx, sy, tx, ty);
        } else {
            int times = (tx - sx) / ty; // Don't go too low -sx
            tx = tx - ty * times;
            if(times == 0){
                return false; // Local min
            }
            c = check(sx, sy, tx, ty);
        }
        return c;
    }
    
public:
    bool reachingPoints(int sx, int sy, int tx, int ty) {
        return check(sx, sy, tx, ty);
    }
};