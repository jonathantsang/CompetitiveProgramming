class Solution {
public:
    string removeDuplicateLetters(string s) {
        unordered_map<char, int> amt;
        for(char c : s){
            if(amt.count(c) > 0){
                amt[c]++;
            } else {
                amt[c] = 1;
            }
        }
        string final = s;
        for(auto it = amt.begin(); it != amt.end(); it++){
            while(it->second > 1){
            // duplicate
                vector<string> possible;
                // find all the possible strings removing this duplicate
                for(int i = 0; i < final.length(); i++){
                    if(final[i] == it->first){
                        string removed = final.substr(0,i) + final.substr(i+1);
                        possible.push_back(removed);
                    }
                }
                // Get the lowest from the possible
                string min = possible[0];
                for(int i = 0; i < possible.size(); i++){
                    if(possible[i] < min){
                        min = possible[i];
                    }
                }
                final = min;
                it->second--;
            }
        }
        return final;
    }
};