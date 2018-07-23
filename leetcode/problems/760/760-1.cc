class Solution {
public:
    vector<int> anagramMappings(vector<int>& A, vector<int>& B) {
        map<int, int> pos;
        for(int i = 0; i < B.size(); i++){
            pos[B[i]] = i;
        }
        vector<int> sol;
        for(int i = 0; i < A.size(); i++){
            sol.push_back(pos[A[i]]);
        }
        return sol;
    }
};