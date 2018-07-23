class Solution {
    int best = 99999;
    map<int, int> seen;
    bool checkneeds(vector<int> &special, vector<int>&needs){
        if(special.size() != needs.size()){
            return false;
        }
        for(int i = 0; i < needs.size(); i++){
            if(special[i] > needs[i]){
                return false;
            }
        }
        return true;
    }
    
    void downwards(vector<int>& price, vector<vector<int>>& special, vector<int>& needs, int costsofar){
        for(int i = 0; i < needs.size(); i++){
            if(needs[i] < 0){
                // invalid
                return;
            }
        }
        
        // First calculate the brute force
        int bfcost = costsofar;
        for(int i = 0; i < price.size(); i++){
            bfcost += price[i] * needs[i];
        }
        // cout << needs[0] << " " << needs[1] << " " << bfcost << endl;
        best = min(best, bfcost);
        
        // Then check for specials and recurse on any one that works
        for(int i = 0; i < special.size(); i++){
            // cout << special[i][0] << " " << special[i][1] << " special "<< endl;
            bool b = checkneeds(special[i], needs);
            if(b){
                for(int j = 0; j < needs.size(); j++){
                    needs[j] -= special[i][j];
                }
                downwards(price, special, needs, special[i].back());
                for(int j = 0; j < needs.size(); j++){
                    needs[j] += special[i][j];
                }
            }
            
        }
    }
public:
    int shoppingOffers(vector<int>& price, vector<vector<int>>& special, vector<int>& needs) {
        int bfcost = 0;
        for(int i = 0; i < price.size(); i++){
            bfcost += price[i] * needs[i];
        }
        best = bfcost;
        
        // Then recurse downwards for valid ones
        downwards(price, special, needs, 0);
        return best;
    }
};