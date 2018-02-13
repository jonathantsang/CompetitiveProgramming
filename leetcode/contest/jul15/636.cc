class Solution {
public:
    map<int, int> ht;
    vector<int> exclusiveTime(int n, vector<string>& logs) {
        ht.clear();
        int lastTime = 0;
        int endTime = 0;
        int leng = logs.size();
        int previous = -1;
        for(int index = 0; index < leng; index++){
            // Start initialize this one has exclusive at least one
            if(logs[index][2] == 's'){
                string et = logs[index].substr(logs[index].size()-1);
                istringstream iss{et};
                iss >> endTime;
                cout << endTime << " endtime for start"<< endl;
                
                // Need to stop previous count
                if(previous != -1){
                    ht[previous] += endTime - lastTime;
                    cout << previous << " adds " << endTime - lastTime << endl;
                }
                
                string pr = logs[index].substr(0,1);
                istringstream is{pr};
                is >> previous;
                
                // Now need to start new count
                // Previous in this case is the new start val
                if(ht.find(previous) == ht.end()){
                    ht[previous] = 1;
                } else {
                    ht[previous] += endTime - lastTime;
                    cout << previous << " adds " << endTime - lastTime << endl;

                }
                
                lastTime = endTime;

            // Add the rest to the end
            } else if (logs[index][2] == 'e'){
                string et = logs[index].substr(logs[index].size()-1);
                istringstream iss{et};
                iss >> endTime;
                cout << endTime << " endtime for end"<< endl;
                
                // Need to stop previous count
                if(previous != -1){
                    ht[previous] += endTime - lastTime;
                    cout << previous << " adds " << endTime - lastTime << endl;
                }
                
                string pr = logs[index].substr(0,1);
                istringstream is{pr};
                is >> previous;
                
                lastTime = endTime;

            }
        }
        // Final hashtable
        vector<int> finale;
        for (auto const& x : ht){
            finale.emplace_back(x.second);
        }
        return finale;
    }
};