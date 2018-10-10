class Solution {
    set<int> possible;
    void recurse(int value, int i, vector<int> &A){
        for(int j = i; j < A.size(); j++){
            int v = value | A[j];
            if(possible.count(v) == 0){
                cout << v << endl;
                cout << "+1" << endl;
                possible.insert(v);
            }
            recurse(v, j+1, A);
        }
    }
public:
    int subarrayBitwiseORs(vector<int>& A) {
        possible.clear();
        vector<int> vals;
        set<int> seen;
        for(int val : A){
            if(seen.count(val) == 0){
                seen.insert(val);
                vals.push_back(val);
            }
        }
        
        // Now recurse on possibilities
        recurse(0, 0, A);
        return possible.size();
    }
};