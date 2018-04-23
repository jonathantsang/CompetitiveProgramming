class Solution {
public:
    int strStr(string haystack, string needle) {
        if(haystack == needle || needle.length() == 0){
            return 0;
        }
        if(haystack.length() < needle.length()){
            return -1;
        }
        for(int i = 0; i < haystack.length(); i++){
            if(haystack[i] == needle[0]){
                // Check the string
                bool valid = true;
                for(int j = 0; j < needle.length(); j++){
                    if(i+j > haystack.length()){
                        valid = false;
                        break;
                    }
                    if(haystack[i+j] != needle[j]){
                        valid = false;
                        break;
                    }
                }
                if(valid){
                    return i;
                }
            }
        }
        return -1;
    }
};