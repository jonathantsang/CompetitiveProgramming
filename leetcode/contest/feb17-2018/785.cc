class Solution {
    bool attempt(map<int,int> s1, map<int, int> s2, vector<vector<int>>& graph, int start){
        int i = start;
        if(start >= graph.size()){
            return true; // Reached end
        }
        
        // No adjacent node
        if(graph[i].size() == 0){
            return attempt(s1, s2, graph, start+1);
        }
        
        else if(s1.find(i) != s1.end()){
            // It is in s1, adjacent must not be in s1 or FAIL
            for(int j = 0; j < graph[i].size(); j++){
                s2[graph[i][j]] = 1;
                if(s1.find(graph[i][j]) != s1.end()){
                    return false;
                }
            }
            // Else fine
            bool a = attempt(s1, s2, graph, start+1);
            return a;
        } else if (s2.find(i) != s2.end()){
            // It is in s2, adjacent must not be in s2 or FAIL
            for(int j = 0; j < graph[i].size(); j++){
                // Add adjacent to s1
                s1[graph[i][j]] = 1;
                if(s2.find(graph[i][j]) != s2.end()){
                    return false;
                }
            }
            // Else fine
            
            bool a = attempt(s1, s2, graph, start+1);
            return a;
        } else {
            map<int, int> copy1 = s1;
            map<int, int> copy2 = s2;
            // Not in either, so have to check both
            // Add to s1, and adj to s2     
            copy1[i] = 1;
            for(int j = 0; j < graph[i].size(); j++){
                copy2[graph[i][j]] = 1;
            }
            bool a1 = attempt(copy1, copy2, graph, start+1);
            
            if(a1){
                return true;
            }
            copy1 = s1;
            copy2 = s2;
            // Add  s2, and adj to s1
            copy2[i] = 1;
            for(int j = 0; j < graph[i].size(); j++){
                copy1[graph[i][j]] = 1;
            }
            bool a2 = attempt(copy1, copy2, graph, start+1);
            
            if(a2){
                return true;
            }
        }
        return false;
    }
public:
    bool isBipartite(vector<vector<int>>& graph) {
        map<int, int> s1;
        map<int, int> s2;
        s1.clear();
        s2.clear();
        bool status = attempt(s1, s2, graph, 0);
        return status;
    }
};