typedef long long int64;
class Solution {
public:
    int minEatingSpeed(vector<int>& a, int H) {
        int n = a.size();
        int low = 1, high = *max_element(a.begin(), a.end());
        while (low != high) {
            int mid = (low + high) / 2;
            int64 sum = 0;
            for (int i = 0; i < n; ++i) {
                sum += (a[i] + mid - 1) / mid;
            }
            if (sum > H) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        return high;
    }
};