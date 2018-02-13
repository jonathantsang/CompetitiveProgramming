class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        char smallest = (char)127;
        bool found = false;
        for(int i = 0; i < letters.size(); i++){
            if(letters[i] > target){
                if(letters[i] <= smallest){
                    smallest = letters[i];
                    found = true;
                }
            }
        }
        if(found){
            cout << "found" << endl;
            return smallest;
        }
        // wrap then
        smallest = (char)1;
        for(int i = 0; i < letters.size(); i++){
            if(letters[i] > smallest){
                return smallest = letters[i];
            }
        }
        return smallest;
    }
};