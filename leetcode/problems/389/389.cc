class Solution {
public:
    char findTheDifference(string s, string t) {
        map<char, int> places; // keeps track of how many
        for(int i = 0; i < s.length(); i++){
            if(places.count(s[i]) < 0){
                places[s[i]] = 1;
            } else {
                places[s[i]] += 1;
            }
        }
        // then go through if the char matches up
        for(int i = 0; i < t.length(); i++){
            if(places.count(t[i]) < 0){
                return t[i];
            } else {
                if(places[t[i]] == 0){
                    return t[i];
                }
                places[t[i]] -= 1;
            }
        }
        // check for the one with 1
        for(map<char,int>::iterator it = places.begin(); it != places.end(); it++){
            if(places[it->first] != 0){
                return it->first;
            }
        }
        return 'a';
    }
};