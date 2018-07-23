class Solution {
    map<int, int> seen; // rooms been to
    void traverse(vector<vector<int>> &rooms, int current){
        if(seen.count(current) > 0){
            // already seen
            return;
        }
        seen[current] = 1;
        for(int i = 0; i < rooms[current].size(); i++){
            // cout << "traverse " << rooms[current][i] << endl;
            traverse(rooms, rooms[current][i]);
        }
    }
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        traverse(rooms, 0);
        // check if all rooms are traversed
        int numRooms = rooms.size();
        // cout << seen.size() << endl;
        return seen.size() == numRooms;
    }
};