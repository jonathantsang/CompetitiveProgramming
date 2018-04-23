class Solution {
    static bool compareLen(string a, string b){
        return (a.length() > b.length()); 
    }
    
    int CheckInString(string ref, string search){
        // cout << "check " << search << " in " << ref << endl; 
        for(int i = 0; i < ref.length(); i++){
            if(ref[i] == search[0]){
                bool found = true;
                // cout << "check " << search << " in " << ref << endl; 
                for(int j = 1; j <= search.length(); j++){
                    // Found word, but need #
                    if(j == search.length()){
                        if(ref[i + j] != '#'){
                            found = false;
                            break;
                        } else {
                            // fine
                            break;
                        }
                    }
                    // cout << "inner " << i << " " << j << endl;
                    // Reached end, could not find it
                    if(i + j >= ref.length()){
                        // cout << search << " failed" << endl;
                        found = false;
                        break;
                    }
                    if(ref[i + j] != search[j]){
                        found = false;
                        break; // Search later
                    }
                }
                if(found){
                    // cout << search << " inside " << ref << endl;
                    return i;
                }
            }
        }
        // cout << search << " failed " << endl;
        // -1 can't find it
        return -1;
    }
public:
    int minimumLengthEncoding(vector<string>& words) {
        // cout << words.size() << endl;
        vector<int> indicies;
        indicies.resize(words.size());
        indicies[0] = 0;
        // sort by length to do longest first
        std::sort(words.begin(), words.end(), compareLen);
        // cout << words[0] << " " << words[1] << endl;
        
        string reference = words[0] + '#';
        
        // Each word after first one
        int chars = reference.length();
        for(int i = 1; i < words.size(); i++){
            chars += words[i].length() + 1; // 1 for #
            // cout << reference << endl;
            // check if word is already in the reference
            int place = CheckInString(reference, words[i]);
            // cout << place << endl;
            if(place == -1){
                // Have to add to the reference
                int oldEnd = reference.length();
                reference += words[i] + '#';
                indicies[i] = oldEnd;
            } else {
                indicies[i] = place;
            }
        }
        // cout << "total of chars " << chars << endl; 
        return reference.length();
    }
};