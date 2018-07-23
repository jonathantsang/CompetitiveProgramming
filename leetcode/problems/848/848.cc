class Solution {
    char shift(char c, int i){
        int a = c + i;
        while(a > 'z'){
            a -= 'z';
        }
        if(a < 'a'){
            a += 'a'-1;
        }
        return a;
    }
public:
    string shiftingLetters(string S, vector<int>& shifts) {
        int total = 0;
        char char_array[20001]; 
        strcpy(char_array, S.c_str()); 
        for(int i = 0; i < shifts.size(); i++){
            total += (shifts[i] % 26);
            total %= 26;
        }
        for(int i = 0; i < S.length(); i++){
            char_array[i] = shift(char_array[i], total);
            // alter to remove for next one
            total -= (shifts[i] % 26);
            total = (total % 26 + 26) % 26;
            //cout << char_array[i] << endl;
            //cout << total << endl;
        }
        string s = string(char_array);
        return s;
    }
};