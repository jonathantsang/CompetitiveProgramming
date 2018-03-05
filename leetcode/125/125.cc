class Solution {
public:
    bool isPalindrome(string s) {
        int start = 0;
        int end = s.length() - 1;
        bool valid = true;
        while(start < end){
            while(!((s[start] >= 'a' && s[start] <= 'z') || (s[start] >= 'A' && s[start] <= 'Z'))){
                if(start + 1 >= s.length()){
                    start++;
                    break;
                }
                start++;
            }
            while(!((s[end] >= 'a' && s[end] <= 'z') || (s[end] >= 'A' && s[end] <= 'Z'))){
                if(end - 1 < 0){
                    end--;
                    break;
                }
                end--;
            }
            cout << start << " " << end << endl;
            if(start >= s.length() || end <= -1){
                break;
            }
            if(tolower(s[start]) != tolower(s[end])){
                valid = false;
                return false;
            }
            start++;
            end--;
        }
        return true;
    }
};