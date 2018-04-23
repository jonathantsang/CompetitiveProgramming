class Solution {
    map<pair<int, int>, int> seen;
    bool recurse(vector<int>&A, int i, int B, int bcount, int C, int ccount){
        // cout << "at " << i << " " << B << " " << C << endl;
        // cout << "counts " << bcount << " " << ccount << endl;
        pair<int, int> p;
        p.first = B* 1000000 + C;
        p.second = i;
        if(seen.find(p) != seen.end()){
            return false; // Seen already
        }
        
        seen[p] = 1;
        float b_calc = 999999;
        float c_calc = 999994;
        if(bcount != 0){
            b_calc = (float) B / (float) bcount;
        }
        if(ccount != 0){
            c_calc = (float) C / (float) ccount;
        }
        cout << b_calc << " " << c_calc << endl;
        if(i >= A.size() && b_calc == c_calc){
            return true;
        }
        if(i >= A.size() && b_calc != c_calc){
            return false;
        }
        // Can give the ith value to B or C
        // give to B
        int B_temp = B + A[i];
        bool b = recurse(A, i+1, B_temp, bcount+1, C, ccount);
        if(b){
            return true;
        }
        
        // give to C
        int C_temp = C + A[i];
        b = recurse(A, i+1, B, bcount, C_temp, ccount+1);
        if(b){
            return true;
        }
        return false;
    }
public:
    bool splitArraySameAverage(vector<int>& A) {
        seen.clear();
        bool possible = recurse(A, 0, 0, 0, 0, 0);
        return possible;
    }
};