class Solution {
public:
    vector<int> splitIntoFibonacci(string S) {
        vector<int> fib;
        if(S.length() <= 2){
            return fib;
        }
        bool valid = true;
        int p1 = S.length()-3;
        int p2 = S.length()-2;
        int p3 = S.length()-1;
        while(valid){
            int a = stoi(S.substr(p1, 1));
            int b = stoi(S.substr(p2, 1))
            int c = stoi(S.substr(p3, 1));   
            if(a + b == c){
                // good then move to solve for a
            } else {
                // check why
                
                // if p3 < p2 + p1
                if(c < a + b){
                    // shift p3 by 1
                    if(p3-1 == p2){
                        if(p2-1 == p1){
                            // shift all by 1
                        }
                    }
                }
                
                else if (c > a + b){
                    
                }
            }
        }
    }
};