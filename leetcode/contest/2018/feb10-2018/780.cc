class Solution {
    map<int, map<int, int>> seen;
    bool check(int sx, int sy, int tx, int ty){
        // Seen it
        if(seen.find(sx) != seen.end()){
            map<int, int> yd = seen[sx];
            if(yd.find(sy) != yd.end()){
                return false;
            }
        }
        //cout << "add " << sx << " " << sy << endl;
        seen[sx][sy] = 1;
        if(sx > tx || sy > ty){
            return false;
        }
        // Check target
        if(sx == tx && sy == ty){
            return true;
        }
        // Not seen yet, mark as seen
        bool p1 = check(sx+sy, sy, tx, ty);
        if(p1){
            return true;
        }
        bool p2 = check(sx, sx+sy, tx, ty);
        if(p2){
            return true;
        }
        return false;
    }
public:
    bool reachingPoints(int sx, int sy, int tx, int ty) {
        seen.clear();
        return check(sx, sy, tx, ty);
    }
};