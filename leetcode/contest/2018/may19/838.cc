class Solution {
    string RLBuilder(int length){
        int each = length / 2;
        if(length % 2 == 0){
            // even
            string s = string(each, 'R') + string(each, 'L');
            return s;
        } else {
            // odd
            string s = string(each, 'R') + '.' + string(each, 'L');
            return s;
        }
    }
public:
    string pushDominoes(string dominoes) {
        string dom = dominoes;
        int lastR = -1;
        int lastL = -1;
        int lastP = -1;
        for(int i = 0; i < dominoes.length(); i++){
            // cout << i << " " << dom << endl;
            // look for groups of RL, or make group for L
            if(dominoes[i] == 'R'){
                lastR = i;
                int storeIndex = i;
                // Find the L
                bool findL = false;
                for(int j = i+1; j < dominoes.length(); j++){
                    storeIndex = j;
                    if(dominoes[j] == 'R'){
                        // skip over
                        lastR = j;
                        i = j;
                    } else if (dominoes[j] == '.'){
                        // make . the R after
                        dom = dom.substr(0, j) + 'R' + dom.substr(j+1);
                    } else if(dominoes[j] == 'L'){
                        dom = dom.substr(0,i) + RLBuilder(j - i + 1) + dom.substr(j+1);
                        findL = true;
                        // update last seen for L, R, .
                        if((j - i + 1) % 2 == 0){
                            // even, so no period
                            lastR = ((j - i + 1) / 2) + i - 1;
                            lastL = lastR + 1;
                            // no update to lastP
                        } else {
                            lastR = ((j - i + 1) / 2) + i - 1;
                            lastP = lastR + 1; // one more than lastR
                            lastL = lastP + 1; // +1 because the .
                        }
                        break;
                    }
                }
                if(findL == false){
                    // never found it so all R
                    string s = string(dominoes.length()-i, 'R');
                    dom = dom.substr(0,i) + s;
                    
                    // update last seen
                    lastR = i+1;
                }
                i = storeIndex;
            } else if (dominoes[i] == 'L'){
                int stopPoint = max(lastR, lastL);
                if(stopPoint == -1){
                    stopPoint = 0;
                }
                
                // Fill as much previously with L
                // replace from stopPoint to i with L
                string s = string(i - stopPoint + 1, 'L');
                dom = dom.substr(0,stopPoint) + s + dom.substr(i+1);
                lastL = i;
            } else {
                // . do nothing
                lastP = i;
            }
        }
        return dom;
    }
};