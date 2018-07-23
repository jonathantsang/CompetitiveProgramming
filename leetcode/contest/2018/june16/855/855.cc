class ExamRoom {
    int last;
    set<int> room;
public:
    ExamRoom(int N) {
        // size should be N
        last = N-1;
    }
    
    int seat() {
        if(room.empty()){
            room.insert(0);
            return 0;
        } else if (room.size() == 1){
            std::set<int>::iterator it=room.begin();            
            if(*it == 0){
                room.insert(last);
                return last;
            } else if (*it == last) {
                room.insert(0);
                return 0;
            } else {
                // Pick better of 0 or last
                int low = *it - 0;
                int high = last - *it;
                if(low > high){
                    room.insert(0);
                    return 0;
                } else {
                    room.insert(last);
                    return last;
                }
            }
        }
        // Go through the set and find the smallest index, biggest difference
        int diff = 0;
        int sit = -1;
        
        // last one first since it is less than earlier in case
        
        if(room.count(last) == 0){
            int mydiff = (last+1) - *prev(room.end()); // space from 10 to last one so like 8
            if(mydiff > diff){
                diff = mydiff;
                sit = last;
            }
        }
           
        for (std::set<int>::iterator it=room.begin(); it != room.end(); ++it){
            if(next(it) == room.end()){
                break;
            }
            int mydiff = *next(it) - *it;
            if(diff < mydiff || diff < mydiff -1){
                diff = mydiff;
                sit = mydiff / 2 + *it;
                // cout << sit << " from " << mydiff << " at " << *it << " next is " << *next(it) << endl;
            }
        }
        
        // Check if 0 is in it
        if(room.count(0) == 0){
            std::set<int>::iterator it=room.begin();
            diff = *it + 1; // minus -1
            sit = 0;
        } 
        
        // cout << "insert " << sit << endl;
        room.insert(sit);
        return sit;
    }
    
    void leave(int p) {
        // cout << "remove " << p << endl;
        room.erase(p);
    }
};

/**
 * Your ExamRoom object will be instantiated and called as such:
 * ExamRoom obj = new ExamRoom(N);
 * int param_1 = obj.seat();
 * obj.leave(p);
 */