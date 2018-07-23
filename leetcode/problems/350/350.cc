class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        vector<int> both;
        map<int, int> count1;
        for(int i = 0; i < nums1.size(); i++){
            if(count1.count(nums1[i]) > 0){
                count1[nums1[i]]++;
            } else {
                count1[nums1[i]] = 1;
            }
        }
        map<int, int> count2;
        for(int i = 0; i < nums2.size(); i++){
            if(count2.count(nums2[i]) > 0){
                count2[nums2[i]]++;
            } else {
                count2[nums2[i]] = 1;
            }
        }
        // then go through each key value and try to get the lowest number for each respective key
        map<int, int> lowest;
        for(auto pair : count1){
            if(count2.count(pair.first) > 0){
                // then pick minimum
                lowest[pair.first] = min(count1[pair.first], count2[pair.first]);
            }
        }
        for(auto pair : lowest){
            for(int i = 0; i < pair.second; i++){
                both.push_back(pair.first);
            }
        }
        return both;
    }
};