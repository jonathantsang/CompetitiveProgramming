class Solution {
    vector<vector<int>> g;
    vector<vector<int>> paths;
    void traverse(int node, int final, vector<int> path){
        cout << "at " << node << endl;
        // Each vertice that node i can direct to
        for(int i = 0; i < g[node].size(); i++){
            if(g[node][i] == final){
                vector<int> newp = path;
                newp.push_back(final);
                paths.push_back(newp);
            } else {
                // Keep looking
                vector<int> newp = path;
                newp.push_back(g[node][i]);
                traverse(g[node][i], final, newp);
            }
        }
    }
public:
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        g = graph;
        paths.clear();
        int nodes = graph.size();
        vector<int> path;
        path.push_back(0);
        traverse(0, nodes-1, path); // start at i
        return paths;
    }
};