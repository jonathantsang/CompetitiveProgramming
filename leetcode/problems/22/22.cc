class Solution {
    vector<string> pairs;
    void Recurse(int i, int max, int l, int r, string comb){
        if(r > l){
            return;
        }
        if(l > max){
            return;
        }
        if(i == max * 2 && r == l){
            pairs.push_back(comb);
            return;
        } else if (i == max * 2 && r != l){
            return;
        }
        // i the index it is currently at
        Recurse(i+1, max, l+1, r, comb+ '(');
        Recurse(i+1, max, l, r+1, comb+ ')');
    }
public:
    vector<string> generateParenthesis(int n) {
        Recurse(0, n, 0, 0, "");
        return pairs;
    }
};