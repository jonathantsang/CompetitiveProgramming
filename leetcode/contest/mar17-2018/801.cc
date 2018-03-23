class Solution {
    void print(vector<vector<int>> dp){
        for(auto row : dp){
            for(int v : row){
                cout << v << " ";
            }
            cout << endl;
        }
        cout << endl;
    }
public:
    int minSwap(vector<int>& A, vector<int>& B) {
        vector<vector<int>> dp; // swap occurs at [i][j] lowest
        dp.resize(A.size());
        for(int i = 0; i < A.size(); i++){
            dp[i].resize(A.size());
        }
        // For swap occuring at i
        for(int i = 0; i < A.size(); i++){
            // Go through j to find best one
            vector<int> A1 = A;
            vector<int> B1 = B;
            A[i] = B[i]; // force swap
            
            // All values beyond
            for(int j = i+1; j < A.size(); j++){
                dp[i][j] = dp[i][j-1]; // Set to previous

                // Check if smaller compared to previous
                if(A1[j] <= A1[j-1]){
                    dp[i][j] = dp[i][j-1] + 1;
                    // Pretend it gets the value
                    int temp = A1[j];
                    A1[j] = B1[j];
                    B1[j] = temp;
                } else if(B1[j] <= B1[j-1]){
                    dp[i][j] = dp[i][j-1] + 1;
                    // Pretend it gets the value
                    int temp = B1[j];
                    B1[j] = A[j];
                    A1[j] = temp;
                }
            }
        }
        print(dp);
        int minimal = INT_MAX;
        for(int i = 0; i < A.size(); i++){
            minimal = min(minimal, dp[i][A.size()-1]);
        }
        return minimal;
    }
};