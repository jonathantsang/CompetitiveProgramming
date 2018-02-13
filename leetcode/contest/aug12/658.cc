class Solution {
    vector<int> answer;
public:
    
    // Compares index1 and index2 in the array to see if the value is there and adds it to vector<int> answer
    void compareTwo(vector<int>& arr, int k, int target, int index1, int index2){
        int leng = arr.size();
        while(k > 0){
            // Check the index1 is >0 and index2 < arr.size() to be valid indicies
            if(index1 < 0){
                answer.emplace_back(arr[index2]);
                index2++;
                k--;
                continue;
            } else if(index2 >= leng){
                answer.emplace_back(arr[index1]);
                index1--;
                k--;
                continue;
            }
        
            // Both should be valid
            int diff1 = abs(target - arr[index1]);
            int diff2 = abs(target - arr[index2]);
            // Check which one is smaller, if they are the same, use the smaller index
            if(diff1 < diff2){
                answer.emplace_back(arr[index1]);
                index1--;
                k--;
                continue;
            } else if (diff2 < diff1){
                answer.emplace_back(arr[index2]);
                index2++;
                k--;
                continue;
            } else if (diff1 == diff2){
                // Assume index1 always has a smaller value than index2
                // Choose index1
                answer.emplace_back(arr[index1]);
                index1--;
                k--;
                continue;
            }
        }
    }
    
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        answer.clear();
        answer.clear();
        int index1 = 0;
        int index2 = 0;
        int leng = arr.size();
        for(int i = 0; i < leng; i++){
            // Check if the value is x
            if(arr[i] == x){
                k -= 1;
                answer.emplace_back(x);
                index1 = i-1;
                index2 = i+1;
                break;
            // Check if the index bound is larger than x, but previous one is smaller, so this is the "imperfect" indices
            } else if (arr[i] > x && arr[i-1] < x){
                index1 = i-1;
                index2 = i;
                break;
            }
        }
        
        // Two edges cases 
        
        // x is less than the first value in arr
        if(x < arr[0]){
            index1 = -1;
            index2 = 0;
        }
        
        // x is greater than the last value in arr
        else if(x > arr[leng-1]){
            index1 = leng-1;
            index2 = leng;
        }
        
        // Run through for each k
        compareTwo(arr, k, x, index1, index2);
        sort(answer.begin(), answer.end());
        return answer;
    }
};