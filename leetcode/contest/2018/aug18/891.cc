class Solution {
    const unsigned int M = 1000000007;
public:
    int sumSubseqWidths(vector<int>& A) {
        int amt = 0;
        for(int i = 0; i < A.size(); i++){
            vector<int> mins(A.size(), 99999);
            vector<int> maxs(A.size(), 0);
            
            // Go through columns
            int idx = 0;
            for(int j = i; j < A.size(); j++){
                if(idx == 0){
                    mins[idx] = A[j];
                    maxs[idx] = A[j];
                    idx++;
                    continue;
                }
                mins[idx] = min(mins[idx-1], A[j]);
                maxs[idx] = max(maxs[idx-1], A[j]);
                idx++;
            }
            
            cout << "mins" << endl;
            for(int a : mins){
                cout << a << " ";
            }
            cout << endl;
            cout << "maxs" << endl;
            for(int b : maxs){
                cout << b << " ";
            }
            cout << endl;
            
            // mins and max vectors now, for each j to A.size(), each time remove back columns
            for(int j = A.size()-1; j >= i; j--){
                int diff = maxs[j] - mins[j];
                amt += diff % M;
            }
        }
        return amt;
    }
};