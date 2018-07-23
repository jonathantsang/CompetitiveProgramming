class Solution {
    bool recurse(string sequence, int counter){
        // check for the sequence ++
        bool end = true;
        for(int i = 0; i < sequence.length()-1; i++){
            if(sequence[i] == '+' && sequence[i+1] == '+'){
                end = false;
                break;
            }
        }
        if(end){
            return counter % 2 == 0;
        }
        // it can go further
        for(int i = 0; i < sequence.length()-1; i++){
            if(sequence[i] == '+' && sequence[i+1] == '+'){
                string a = sequence.substr(0, i) + "--" + sequence.substr(i+2);
                bool result = recurse(a, counter+1);
                if(result){
                    return result;
                }
            }
        }
        return false;
    }

public:
    bool canWin(string s) {
        return recurse(s,0);
    }
};