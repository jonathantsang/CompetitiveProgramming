class Solution {
    static bool comp(pair<int, int> &a, pair<int, int> &b){
        return a.first != b.first ? a.first >= b.first : a.second < b.second;
    }
public:
    vector<pair<int, int>> reconstructQueue(vector<pair<int, int>>& people) {
        vector<pair<int,int>> queue;
        sort(people.begin(), people.end(), comp);
        /*for(auto p : people){
            cout << p.first << " " << p.second << endl;
        }*/
        for(pair<int, int> p : people){
            queue.insert(queue.begin() + p.second, p);
        }
        return queue;
    }
};