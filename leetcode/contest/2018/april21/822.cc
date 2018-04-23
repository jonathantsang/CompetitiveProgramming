class Solution {
public:
    int flipgame(vector<int>& fronts, vector<int>& backs) {
        map<int,int> lock;
        int lowest = 2001;
        // each one check for deadlock
        for(int i = 0; i < fronts.size(); i++){
            if(fronts[i] == backs[i]){
                lock[fronts[i]] = 1; 
                // means that for fronts[i], it cannot be a lowest since a swap will cause it to be in
                // front and back
            }
        }
        // each front
        for(int i = 0; i < fronts.size(); i++){
            // check if lock
            if(lock.find(fronts[i]) == lock.end()){
                lowest = min(lowest, fronts[i]);
            }
        }
        // each back
        for(int i = 0; i < backs.size(); i++){
            // check if lock
            if(lock.find(backs[i]) == lock.end()){
                lowest = min(lowest, backs[i]);
            }
        }
        if(lowest == 2001){
            return 0;
        } else {
            return lowest;
        }
    }
};