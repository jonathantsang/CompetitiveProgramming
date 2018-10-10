class Solution {
public:
    vector<string> findAndReplacePattern(vector<string>& words, string pattern) {
        vector<string> ans;
        
        char start = 'a';
        unordered_map<char, char> pMapping;
        string patternMap;
        for(char c : pattern){
            if(pMapping.count(c) == 0){
                patternMap += start;
                pMapping[c] = start;
                start++;
            } else {
                patternMap += pMapping[c];
            }
        }
        // Now we have a pattern mapped to first use
        
        for(string word : words){
            bool inside = true;
            
            char count = 'a';
            unordered_map<char, int> mapping;
            string constructed;
            int i = 0;
            for(char c : word){
                if(mapping.count(c) == 0){
                    constructed += count;
                    if(patternMap[i] != count){
                        inside = false;
                    }
                    mapping[c] = count;
                    count++;
                    i++;
                } else {
                    constructed += mapping[c];
                    if(patternMap[i] != mapping[c]){
                        inside = false;
                    }
                    i++;
                }
            }
            
            // use inside
            if(inside){
                ans.push_back(word);
            }
        }
        return ans;
    }
};