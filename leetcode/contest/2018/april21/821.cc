class Solution {
    int closest(string S, char C, int p){
        int dist = 10001;
        // Rightward
        for(int i = p; i < S.length(); i++){
            if(S[i] == C){
                dist = min(dist, i - p);
            }
        }
        for(int i = p; i >= 0; i--){
            if(S[i] == C){
                dist = min(dist, p - i);
            }
        }
        return dist;
    }
public:
    vector<int> shortestToChar(string S, char C) {
        vector<int> dist;
        dist.resize(S.length());
        for(int i = 0; i < S.length(); i++){
            dist[i] = closest(S, C, i);
        }
        return dist;
    }
};