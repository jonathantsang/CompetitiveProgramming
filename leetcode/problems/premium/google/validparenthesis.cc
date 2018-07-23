class Solution {
public:
    bool isValid(string s) {
        vector<int> stack; 
        for(int i = 0; i < s.length(); i++){
            if(s[i] == '('){
                stack.push_back(1);
            } else if (s[i] == '{'){
                stack.push_back(2);
            } else if (s[i] == '['){
                stack.push_back(3);
            } else if (s[i] == ')'){
                if(stack.size() <= 0) return false;
                int val = stack.back();
                if(val != 1){
                    return false;
                }
                stack.pop_back();
            } else if (s[i] == '}'){
                if(stack.size() <= 0) return false;
                int val = stack.back();
                if(val != 2){
                    return false;
                }
                stack.pop_back();
            } else if (s[i] == ']'){
                if(stack.size() <= 0) return false;
                int val = stack.back();
                if(val != 3){
                    return false;
                }
                stack.pop_back();
            }
        }
        return stack.size() == 0;
    }
};