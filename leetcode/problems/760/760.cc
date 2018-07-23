class Solution {
public:
    vector<int> anagramMappings(vector<int>& A, vector<int>& B) {
        vector<int> mapping;
        map<int, int> placeInB; // keeps track of place in B
        
        for(int i = 0; i < B.size(); i++){
            placeInB[B[i]] = i; // stores the place of the element
        }
        for(int i = 0; i < A.size(); i++){
            mapping.push_back(placeInB[A[i]]);
        }
        return mapping;
    }
};