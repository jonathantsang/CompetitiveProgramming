class Solution {
    map<string, int> ht;
public:
    bool recurse(string current, string end){
        for(int i = 0; i < current.length(); i++){
            string newstring = "";
            // check for replace
            // LX
            if(i+1 < current.length() && current[i] == 'X' && current[i+1] == 'L'){
                newstring = current.substr(0, i) + "LX" + current.substr(i+2);
                // cout << newstring << endl;
                // cout << current << endl;
            // XR
            } else if (i+1 < current.length() && current[i] == 'R' && current[i+1] == 'X'){
                // cout << current.substr(0, i) << " " << "XR" << " " << current.substr(i+2) << endl;
                newstring = current.substr(0, i) + "XR" + current.substr(i+2);
            }
            if(newstring == ""){
                continue;
            }
            if(newstring == end){
                return true;
            }
            // Already seen
            // cout << newstring << endl;
            if(ht.find(newstring) != ht.end()){
                continue;
            } else {
                ht[newstring] = 1;
            }
            if(recurse(newstring, end)){
                return true;
            }
        }
        return false;
    }
    
    bool canTransform(string start, string end) {
        ht.clear();
        if(start == end){
            return true;
        }
        map<char, int> count;
        for(int i = 0; i < start.length(); i++){
            if(count.find(start[i]) == count.end()){
                count[start[i]] = 1;
            } else {
                count[start[i]] += 1;
            }
        }
        map<char, int> counte;
        for(int i = 0; i < end.length(); i++){
            if(counte.find(end[i]) == counte.end()){
                count[end[i]] = 1;
            } else {
                count[end[i]] += 1;
            }
        }
        // Make sure count of L, X, and R are equal
        for(map<char,int>::iterator it = count.begin(); it != count.end(); ++it) {
            if(count[it->first] != count[it->first]){
                return false;
            }
        }
        
        return recurse(start, end);
    }
};