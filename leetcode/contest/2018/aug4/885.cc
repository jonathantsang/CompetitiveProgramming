class Solution {
    // -1 if not found
    int binSearch(int look, vector<int> &people, int start, int end){
        // cout << "look for " << look << endl;
        // cout << "start " << start << " " << "end " << end << endl;
        int idx = start;
        while(end > start){
            int mid = (start + end) / 2;
            
            // arr is flipped so do opposite of bin search
            if(people[mid] > look){
                // go right
                start = mid+1;
            } else {
                // go left
                end = mid;
            }
        }
        if(start >= people.size() || people[start] > look){
            return -1;
        }
        // cout << "found " << people[start] << endl;
        return start;
    }
    
public:
    int numRescueBoats(vector<int>& people, int limit) {
        int boats = 0;
        sort(people.begin(), people.end(), greater<int>());
                
        // Go through each people weight and bin search best match
        while(people.size() >= 1){
            if(people.size() == 1){
                boats++;
                break;
            }
            
            int top = people.front();
            
            if(top == limit){
                boats++;
                people.erase(people.begin());
                continue;
            }
            
            int valueIndex = binSearch(limit - top, people, 1, people.size());
            // remove value from the binSearch
            if(valueIndex != -1){
                // cout << "remove at " << valueIndex << endl;
                people.erase(people.begin()+valueIndex);
            }
            people.erase(people.begin());
            boats++;
        }
        return boats;
    }
};