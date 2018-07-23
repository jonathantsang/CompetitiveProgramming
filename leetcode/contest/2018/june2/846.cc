class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int W) {
        if(hand.size() % W != 0) return false;
        bool valid = true;
        sort(hand.begin(), hand.end());
        while(valid){
            // get group of W from the front
            map<int, int> groupOfW;
            int i = hand.size()-1; // denote where
            int amt = 0;
            int last = -1;
            while(i >= 0 && amt < W){
                // cout << "last " << last << " " << i << endl;
                if(last == -1 && groupOfW.count(hand[i]) == 0){
                    groupOfW.count(hand[i]); // add the number to the subset
                    last = hand[i];
                    hand.erase(hand.begin() + i);
                    i--;
                    amt++;
                }
                else if(hand[i] + 1 == last && groupOfW.count(hand[i]) == 0){
                    groupOfW.count(hand[i]); // add the number to the subset
                    last = hand[i];
                    hand.erase(hand.begin() + i);
                    i--;
                    amt++;
                } else {
                    // skip it and move on
                    i--;
                }
                // cout << "last " << last << " " << i << endl;
            }
            if(i == -1 && hand.size() != 0){
                // went through all and couldn't find any
                return false;
            } else if(i == -1 && hand.size() == 0){
                return true;
            }
        }
        return true;
    }
};