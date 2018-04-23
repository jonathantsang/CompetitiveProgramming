class Solution {
    float execute(vector<int> &A, map<int, int> &partitions){
        float total = 0;
        float portion = 0;
        float size = 0;
        for(int i = 0; i < A.size(); i++){
            if(partitions.find(i) != partitions.end()){
                // portion average
                portion += A[i];
                size++;
                // cout << i << " new portion " << portion << endl;
                total += (portion / size);
                // cout << "total is " << total << endl;
                portion = 0;
                size = 0;
            } else {
                // cout << "not a partition spot" << endl;
                portion += A[i];
                //cout << "portion is " << portion << endl;
                size++;
            }
            
        }
        if(size == 0){
            return total;
        }
        // cout << portion / size << endl;
        total += (portion / size);
        // cout << "total is " << total << endl;
        return total;
    }
public:
    double largestSumOfAverages(vector<int>& A, int K) {
        float total = 0;
        if(K == A.size()){
            // Each in its own group
            for(int i = 0; i < A.size(); i++){
                total += A[i];
            }
            return total;
        } else if (K == 1){
            // Each in its own group
            for(int i = 0; i < A.size(); i++){
                total += A[i];
            }
            return total / A.size();
        } else {
            map<int, int> partitions; // 0 means it splits 0 from rest of array
            // Need to partition in groups, find best place for each count
            // K-1 partitions for K groups
            for(int i = 0; i < K-1; i++){
                // Find best placement
                vector<int> choose;
                choose.resize(A.size());
                fill(choose.begin(), choose.end(), 0);
                for(int j = 0; j < A.size(); j++){
                    if(partitions.find(j) != partitions.end()){
                        // skip this number, already a partition there
                        continue;
                    }
                    map<int, int> new_p = partitions;
                    new_p[j] = 1;
                    choose[j] = execute(A, new_p);
                }
                // Pick best place for partition based on choose
                int index = 0;
                int maxval = 0;
                for(int j = 0; j < A.size(); j++){
                    if(choose[j] > maxval){
                        maxval = choose[j];
                        index = j;
                    }
                }
                partitions[index] = 1;
                // cout << "new partition at " << index << endl;
            }
            // cout << "final one " << endl;
            total = execute(A, partitions);
            // cout << total << endl;
            double d = static_cast<double>(total);
            // cout << d << endl;
            return d;
        }
        return 0;
    }
};