class Solution {
public:
    int binaryGap(int N) {
        string binary = bitset<64>(N).to_string();
        // find front 1 and end 1
        int start = -1;
        int end = -1;
        int maxDist = 0;
        for(int i = 0; i < binary.length(); i++){
            if(binary[i] == '1' && start == -1){
                start = i;
            } else if (binary[i] == '1') {
                end = i;
                maxDist = max(maxDist, end - start);
                start = i;
            }
        }
        return maxDist;
    }
};