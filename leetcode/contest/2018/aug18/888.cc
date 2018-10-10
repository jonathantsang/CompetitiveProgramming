class Solution {
public:
    vector<int> fairCandySwap(vector<int>& A, vector<int>& B) {
        vector<int> ans;
        int aSum = 0;
        int bSum = 0;
        set<int> aVals;
        set<int> bVals;
        for(int v: A){
            aSum += v;
            aVals.insert(v);
        }
        for(int v: B){
            bSum += v;
            bVals.insert(v);
        }
        int diff = aSum - bSum;
        int absDiff = abs(diff);
        int halfAbsDiff = absDiff / 2;
        if(diff < 0){
            // bSum is bigger, go through aSum checking larger by halfAbsDiff
            for(int v : A){
                if(bVals.count(v+halfAbsDiff) != 0){
                    ans.push_back(v);
                    ans.push_back(v+halfAbsDiff);
                    return ans;
                }
            }
            // should find something
        } else {
            // aSum is bigger, go through bSum checking larger by halfAbsDiff
            for(int v : B){
                if(aVals.count(v+halfAbsDiff) != 0){
                    ans.push_back(v+halfAbsDiff);
                    ans.push_back(v);
                    return ans;
                }
            }
        }
        return ans;
    }
};