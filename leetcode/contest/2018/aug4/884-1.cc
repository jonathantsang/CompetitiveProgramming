class Solution {
public:
    string decodeAtIndex(string S, int K) {
        int N = S.length();
        while(K >= 0) {
            //cout << K << endl;
            long long prev = 0LL, curr = 0LL;
            for(int i=0; i<N; i++) {
                if('0' <= S[i] && S[i] <= '9') {
                    curr = prev*(S[i]-'0');
                    if(curr >= K) {
                        K = ((K-1) % prev) + 1;
                        break;
                    }
                }
                else {
                    curr++;
                    if(curr >= K) {
                        return S.substr(i, 1);
                    }
                }
                prev = curr;
            }
        }
    }
};