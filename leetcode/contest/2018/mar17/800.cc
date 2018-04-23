class Solution {
    char pick(string s){
        char ch1;
        char chplus;
        char chminus;
        int original = stoi(s, nullptr, 16);
        int number = original;
        int val = (number / 16) * 16 + number / 16;
        int valminusone = ((number / 16) - 1) * 16 + ((number / 16) - 1);
        int valplusone = ((number / 16) + 1) * 16 + ((number / 16) + 1);
    
        if(valplusone > 256){
            valplusone = 99999;
        }
        if(valminusone < 0){
            valminusone = 999999;
        }
        int minimal = min(abs(original - valminusone), min(abs(original - val), abs(original - valplusone)));
        // cout << "minimal is " << minimal << endl;
        if(minimal == abs(original - val)){
            return s[0];
        } else if (minimal == abs(original - valminusone)){
            if(s[0] == 'a'){
                return '9';
            }
            return s[0]-1;
        } else if (minimal == abs(original - valplusone)){
            if(s[0] == '9'){
                return 'a';
            }
            return s[0]+1;
        } else {
            cout << "bad" << endl;
            return s[0];
        }
    }
public:
    string similarRGB(string color) {
        string c1 = color.substr(1,2);
        string c2 = color.substr(3,2);
        string c3 = color.substr(5,2);
        string rgb = "";
        stringstream ss;
        // Get first one
        char a1 = pick(c1);
        char a2 = pick(c2);
        char a3 = pick(c3);
        string final = "";
        final += '#';
        final += a1;
        final += a1;
        final += a2;
        final += a2;
        final += a3;
        final += a3;
        return final;
    }
};