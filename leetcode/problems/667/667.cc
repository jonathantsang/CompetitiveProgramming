class Solution {
public:
    vector<int> constructArray(int n, int k) {
        vector<int> arr;
        // k == 1
        if(k == 1){
            for(int i = 1; i <= n; i++){
                arr.push_back(i);
            }
        } else if (k == 2){
            for(int i = 2; i <= n; i++){
                arr.push_back(i);
            }
            arr.push_back(1);
        } else if (k > 2){
            // 3 or greater
            // 1 big or greater
            int top = n;
            int bottom = 1;
            int excl = 0;
            while(excl < k-1){
                arr.push_back(bottom);
                arr.push_back(top);
                bottom++;
                top--;
                excl+=2;
            }
            // Then if it is k % 2 == 0, reverse, else k % 2 == 1 in order 
            if(k % 2 == 0){
                for(int i = top; i >= bottom; i--){
                    arr.push_back(i);
                }
            } else {
               for(int i = bottom; i <= top; i++){
                    arr.push_back(i);
                } 
            }
        }
        return arr;
    }
};