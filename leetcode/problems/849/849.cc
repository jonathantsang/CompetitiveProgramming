class Solution {
    vector<int> taken;
public:
    int maxDistToClosest(vector<int>& seats) {
        taken.clear();
        for(int i = 0; i < seats.size(); i++){
            if(seats[i] == 1){
                taken.push_back(i);
            }
        }
        // Now we know the seats taken, keep track of last seen taken and next taken
        int last = -1;
        int end = -1;
        if(taken.size() != 1){
            end = 0;
        }
        // Now go through the seats and check the last and end at each point
        int bestDist = 0;
        for(int i = 0; i < seats.size(); i++){
            // cout << i << " i " << last << " " << end << " le" << endl;
            if(seats[i] == 1){
                // Bump up the last and end (if applicable)
                last++;
                if(end != -1){
                    end++;
                }
                if(end >= taken.size()){
                    end = -1;
                }
            } else {
                // Not started first one yet
                if(last == -1){
                    int leftway = taken[0] - i;
                    bestDist = max(bestDist, leftway);
                    continue;
                }
                
                // cout << "last " << last << " " << "end " << end << endl;
                
                // Calculate the best last and end
                int leftway = i - taken[last];
                int rightway = 999999;
                if(end != -1){
                    rightway = taken[end] - i;
                }
                bestDist = max(bestDist, min(leftway, rightway));
            }
            // cout << i << " " << bestDist << endl;
        }
        return bestDist;
    }
};