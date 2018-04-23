class Solution {
public:
    int uniqueMorseRepresentations(vector<string>& words) {
        // map
        vector<string> m{".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
        
        map<string, int> morse_count;
        int total = 0;
        // For each word
        for(int i = 0; i < words.size(); i++){
            // For each char in word
            string morse_word = "";
            for(int j = 0; j < words[i].size(); j++){
                int index = words[i][j] - 97;
                morse_word += m[index];
            }
            
            // Check in map of made
            if(morse_count.find(morse_word) == morse_count.end()){
                morse_count[morse_word] = 1;
                total++;
            } else {
                morse_count[morse_word]++;
            }
        }
        return total;
    }
};