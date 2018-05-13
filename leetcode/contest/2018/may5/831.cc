class Solution {
public:
    string maskPII(string S) {
        if((S[0] >= 'a' && S[0] <= 'z') || (S[0] >= 'A' && S[0] <= 'Z')){
            // email
            
            char alpha = S[0];
            // lowercase, first five * and @
            if(S[0] >= 'A' && S[0] <= 'Z'){
                alpha += 32;
            }
            string email;
            email += alpha;
            email += "*****";
            int keep = 0;
            // cout << email << " ada "<< endl;
            for(int i = 1; i < S.length(); i++){
                if(S[i] == '@'){
                    // get last character
                    char last = S[i-1];
                    if(S[i-1] >= 'A' && S[i-1] <= 'Z'){
                        last += 32;
                    }
                    email += last;
                    keep = i;
                    // email += S.substr(i);
                    break;
                }
            }
            for(int i = keep; i < email.length(); i++){
                char alpha = S[i];
                if(S[i] >= 'A' && S[i] <= 'Z'){
                    alpha += 32;
                }
                email += alpha;
            }
            // cout << email << endl;
            return email;
        } else {
            // number
            string email;
            string number;
            for(int i = 0; i < S.length(); i++){
                if(S[i] >= '0' && S[i] <= '9'){
                    number += S[i];
                }
            }
            // normal
            if(number.length() == 10){
                email += "***";
                email += '-';
                email += "***";
                email += '-';
                email += number.substr(6,4);
            } else {
                // first two country code, then number
                int len = number.length() - 10;
                string cc = number.substr(0, len);
                if(len == 1){
                    cc = "*";
                } else if (len == 2){
                    cc = "**";
                } else if (len == 3){
                    cc = "***";
                }
                number = number.substr(len);
                email += '+';
                email += cc;
                email += '-';
                email += "***";
                email += '-';
                email += "***";
                email += '-';
                email += number.substr(6,4);
            }
            // cout << email << endl;
            return email;
        }
    }
};