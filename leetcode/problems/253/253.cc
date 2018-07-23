/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
class Solution {
public:
    int minMeetingRooms(vector<Interval>& intervals) {
        map<int, int> changes;
        for(Interval meeting : intervals){
            changes[meeting.start] += 1;
            changes[meeting.end] -= 1;
        }
        int room = 0;
        int maxrooms = 0;
        for(auto change : changes){
            maxrooms = max(maxrooms, room += change.second);
        }
        return maxrooms;
    }
};