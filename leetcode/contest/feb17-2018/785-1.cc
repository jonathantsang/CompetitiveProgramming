class Solution {
    bool run(map<int, int> s1, map<int, int> s2, vector<vector<int>>& graph, int i){
        //cout << "attempt " << i << endl;
        if(i >= graph.size()){
            return true;
        } else if (graph[i].size() == 0){
            // Assume sorted
            return run(s1, s2, graph, i+1);
        }
        // True for putting i into that set, starts true
        bool in1 = true;
        bool in2 = true;
        
        if(s1.find(i) != s1.end()){
            // In s1
            //cout << "not s2 for " << i << endl;
            in2 = false;
        } else if (s2.find(i) != s2.end()){
            // In s2
            //cout << "not s1 for " << i << endl;
            in1 = false;
        }
        // Each value in the adjacent list of i
        for(int j = 0; j < graph[i].size(); j++){
            // Puts false if the adj value is found in the set
            if(s1.find(graph[i][j]) != s1.end()){
                in1 = false;
            } else if (s2.find(j) != s2.end()){
                in2 = false;
            }
        }
        //cout << "in1- " << in1 << " in2- " << in2 << endl;
        if(in1 && !in2){
            //cout << "s1 for " << i << endl;
            // Put i in s1 and adj in s2
            s1[i] = 1;
            for(int j = 0; j < graph[i].size(); j++){
                s2[graph[i][j]] = 1;
            }
            return run(s1, s2, graph, i+1);
        } else if (!in1 && in2){
            //cout << "s2 for " << i << endl;
            // Put i in s2 and adj in s1
            s2[i] = 1;
            for(int j = 0; j < graph[i].size(); j++){
                s1[graph[i][j]] = 1;
            }
            return run(s1, s2, graph, i+1);
        } else if (!in1 && !in2){
            // Can't
            return false;
        } else if (in1 && in2){
            // Either
            //cout << "either for " << i << endl;
            // Temp
            map<int, int> c1 = s1;
            map<int, int> c2 = s2;
            
            // Put i in s1 and adj in s2
            s1[i] = 1;
            for(int j = 0; j < graph[i].size(); j++){
                s2[graph[i][j]] = 1;
            }
            bool a1 = run(s1, s2, graph, i+1);
            if(a1){
                return true;
            }
            //cout << "try again" << endl;
            s1 = c1;
            s2 = c2;
            // Put i in s2 and adj in s1
            s2[i] = 1;
            for(int j = 0; j < graph[i].size(); j++){
                s1[graph[i][j]] = 1;
            }
            bool a2 = run(s1, s2, graph, i+1);
            if(a2){
                return true;
            }
        }
        return false;
    }   
    
public:
    bool isBipartite(vector<vector<int>>& graph) {
        // sort(graph.begin(), graph.end(), [](const vector<int> & a, const vector<int> & b){ return a.size() > b.size(); });
        /*
        for(int i = 0; i < graph.size(); i++){
            cout << "for " << i << " ";
            for(int j = 0; j < graph[i].size(); j++){
                cout << graph[i][j] << " ";
            }
            cout << endl;
        }*/
        map<int, int> s1;
        map<int, int> s2;
        s1.clear();
        s2.clear();
        bool ans = run(s1, s2, graph, 0);
        return ans;
    }
};