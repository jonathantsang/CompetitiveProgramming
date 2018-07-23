class Solution {
public:
    bool isPalindrome(string s) {
        if(s == ""){
            return true;
        }
        if(s.length() <= 1){
            return true;
        }
        int start = 0;
        int end = s.length()-1;
        while(!(s[start] >= 'a' && s[start] <= 'z') && !(s[start] >= 'A' && s[start] <= 'Z') && 
              !(s[start] >= '0' && s[start] <= '9')){
            start++;
            if(start > s.length()){
                break;
            }
        }
        while(!(s[end] >= 'a' && s[end] <= 'z') && !(s[end] >= 'A' && s[end] <= 'Z') &&
             !(s[end] >= '0' && s[end] <= '9')){
            end--;
            if(end < 0){
                break;
            }
        }
        while(start < end){
            char a = s[start];
            char b = s[end];
            if(tolower(a) != tolower(b)){
                return false;
            } else {
                start++;
                while(!(s[start] >= 'a' && s[start] <= 'z') && !(s[start] >= 'A' && s[start] <= 'Z') &&
                     !(s[start] >= '0' && s[start] <= '9')){
                    start++;
                    if(start > s.length()){
                        break;
                    }
                }
                end--;
                while(!(s[end] >= 'a' && s[end] <= 'z') && !(s[end] >= 'A' && s[end] <= 'Z') &&
                     !(s[end] >= '0' && s[end] <= '9')){
                    end--;
                    if(end < 0){
                        break;
                    }
                }             
            }
        }
        return true;
    }
};