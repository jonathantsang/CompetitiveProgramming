class Solution {
    vector<int> remove;
    map<int, int> lastSeen;
    map<int, vector<int>> adjlist;
    void traverse(int i, int prev){
        // dfs on the children
        if(lastSeen.count(i) > 0){
            // seen already, meaning the edge in lastSeen is the edge we want
            remove.push_back(lastSeen[i]);
            remove.push_back(i);
            return;
        }
        lastSeen[i] = prev;
        
        // traverse children
        for(int j = 0; j < adjlist[i].size(); j++){
            // last seen connection to it
            traverse(adjlist[i][j], i);
        }
    }
public:
    vector<int> findRedundantDirectedConnection(vector<vector<int>>& edges) {
        remove.clear();
        lastSeen.clear();
        adjlist.clear();
        // find the root where no node goes to it
        map<int, int> count;
        for(int i = 0; i < edges.size(); i++){
            adjlist[edges[i][0]].push_back(edges[i][1]);
            count[edges[i][1]] = 1;
        }
        int root = -1;
        for(int i = 0; i < edges.size(); i++){
            // check which outgoing edge is not in count
            if(count.count(edges[i][0]) == 0){
                root = edges[i][0];
                break;
            }
        }
        traverse(root, -1);
        // Then
        return remove;
    }
};