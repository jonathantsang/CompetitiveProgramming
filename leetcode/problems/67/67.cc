class Solution {
public:
    string addBinary(string a, string b) {
        string merge = "";
        int index = 0; // From the right
        int carry = 0;
        while(index < a.length() || index < b.length()){
            //cout << "index " << index << endl;
            if(index >= a.length()){
                char bit = b[b.length()-1-index] == '1' ? '1' : '0';
                if(carry){
                    if(bit == '1'){
                        carry = 1;
                        bit = '0';
                    } else {
                        carry = 0;
                        bit = '1';
                    }
                }
                merge = bit + merge;
            } else if (index >= b.length()){
                char bit = a[a.length()-1-index] == '1' ? '1' : '0';
                if(carry){
                    if(bit == '1'){
                        carry = 1;
                        bit = '0';
                    } else {
                        carry = 0;
                        bit = '1';
                    }
                }
                merge = bit + merge;
            } else {
                char bit = a[a.length()-1-index] == b[b.length()-1-index] ? '0' : '1';
                if(carry){
                    if(bit == '1'){
                        carry = 1;
                        bit = '0';
                    } else {
                        carry = 0;
                        bit = '1';
                    }
                }
                if(a[a.length()-1-index] == '1' && b[b.length()-1-index] == '1'){
                    carry = 1;
                } else {
                    carry = 0;
                }
                merge = bit + merge;
            }
            //cout << "m " << merge << endl;
            index++;
        }
        if(carry == 1){
            merge = '1' + merge;
        }
        return merge;
    }
};