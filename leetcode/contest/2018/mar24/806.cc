class Solution {
public:
    vector<int> numberOfLines(vector<int>& widths, string S) {
        int lines = 0;
        int hund = 0;
        for(int i = 0; i < S.length(); i++){
            int index = S[i] - 97;
            if(hund + widths[index] > 100){
                hund = widths[index];
                lines++;
            } else if (hund + widths[index] == 100){
                hund = 0;
                lines++;
            } else {
                hund += widths[index];
            }
        }
        
        int overflow = hund;
        if(overflow != 0){
            lines++;
        }
        
        vector<int> final;
        final.emplace_back(lines);
        final.emplace_back(overflow);
        return final;
    }
};