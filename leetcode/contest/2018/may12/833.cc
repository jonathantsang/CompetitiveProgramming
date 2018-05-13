class Solution {
public:
    string findReplaceString(string S, vector<int>& indexes, vector<string>& sources, vector<string>& targets) {
        vector<int> counts (1001, 0);
        // perform actions on the string
        string newstring = S;
        for(int i = 0; i < indexes.size(); i++){
            // cout << newstring << endl;
            int len = sources[i].length();
            if(S.substr(indexes[i], len) == sources[i]){
                // cout << "succ" << endl;
                int offset = 0;
                
                // calculate offset
                for(int j = 0; j < indexes[i]; j++){
                    // add up since the new things affect it
                    offset += counts[j];
                }
                
                //cout << "offset " << offset << endl;
                
                // offset indexes[i] by amount previously offset
                newstring = newstring.substr(0,indexes[i]+offset) + targets[i] + newstring.substr(indexes[i]+ offset + len);
                
                // everything greater than index of indexes[i], needs to increase by len, or decrease
                counts[indexes[i]] += targets[i].length() - sources[i].length();
                //cout << targets[i].length() << " added for " << indexes[i] << endl;
                // cout << "new counts for " << indexes[i] << " is " << counts[indexes[i]] << endl;
            }
            
        }
        //cout << newstring << endl;
        return newstring;
    }
};