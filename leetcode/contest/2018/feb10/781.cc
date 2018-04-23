class Solution {
    map<int, int> counts;
public:
    int numRabbits(vector<int>& answers) {
        int amt = 0;
        for(int i = 0; i < answers.size(); i++){
            if(counts.find(answers[i]) == counts.end()){
                counts[answers[i]] = 1;
            } else {
                counts[answers[i]] += 1;
            }
        }
        map<int, int>::iterator it = counts.begin();
        for(; it != counts.end(); it++){
            int bunch = it->first + 1;
            int groupsneeded = (it->second / bunch);
            // Overflow needed for group
            if(it->second % bunch != 0){
                groupsneeded++;
            }
            // cout << groupsneeded << endl;
            amt += groupsneeded * bunch;            
        }
        return amt;
    }
};