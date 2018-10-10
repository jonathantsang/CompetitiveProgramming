class Solution {
public:
    vector<string> uncommonFromSentences(string A, string B) {
        vector<string> uncommon;
        map<string, int> wordsA;
        istringstream iss{A};
        string word;
        while(iss >> word){
            if(wordsA.count(word) == 0){
                wordsA[word] = 1;
            } else {
                wordsA[word]++;
            }
        }
        map<string, int> wordsB;
        istringstream issb{B};
        while(issb >> word){
            if(wordsB.count(word) == 0){
                wordsB[word] = 1;
            } else {
                wordsB[word]++;
            }
        }
        // find all not in one
        for(auto p : wordsA){
            if(p.second == 1 && wordsB.count(p.first) == 0){
                uncommon.push_back(p.first);
            }
        }
        for(auto p : wordsB){
            if(p.second == 1 && wordsA.count(p.first) == 0){
                uncommon.push_back(p.first);
            }
        }
        return uncommon;
    }
};