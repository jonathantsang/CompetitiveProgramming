class Solution {
    int checkRow(vector<int> &piles, int H, int mmin, int mmax){
        while(mmax > mmin){
            bool good = true;
            int K = (mmax + mmin) / 2;
            int hours = 0;
            for(int i = 0; i < piles.size(); i++){
                int h = piles[i] / K;
                h = piles[i] % K == 0 ? h : h+1;
                hours += h;
                if(hours > H){
                    good = false;
                    break;
                }
            }
            if(good){
                mmax = K;
            } else {
                mmin = K+1;
            }
        }
        return mmin;
    }
public:
    int minEatingSpeed(vector<int>& piles, int H) {
        int mmin = -1;
        int mmax = -1;
        for(int i = 0; i < piles.size(); i++){
            if(mmin == -1){
                mmin = piles[i];
            }
            mmin = min(piles[i], mmin);
            mmax = max(piles[i], mmax);
        }
        // bin search
        int val = checkRow(piles, H, mmin, mmax);
        return val;
    }
};