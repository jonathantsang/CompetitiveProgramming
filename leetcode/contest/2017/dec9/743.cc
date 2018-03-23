class Solution {
    class Edge;
    map<int, int> reached;
    map<int, vector<Edge*>> nodes;
    vector<Edge*> edgesintransition;
    int time;
    int num;
    class Edge{
        public:
        int source;
        int target;
        int time;
        Edge(int s, int ta, int ti):source{s},target{ta},time{ti}{}
    };
    
public:
    bool checkDone(){
        int N = num;
        // check that all are marked from 1 to N
        for(int i = 1; i <= N; i++){
            if(reached[i] != 1){
                return false;
            }
        }
        return true;
    }
    
    void sendSig(int nodeval){
        vector<Edge*> outwardedges = nodes[nodeval];
        reached[nodeval] = 1; // reached at current
        bool done = checkDone();
        if(done){
            time = 0;
            return;
        }
        int timesofar = 0;

        // Add traversing to in transit
        for(int i = 0; i < outwardedges.size(); i++){
            edgesintransition.emplace_back(outwardedges[i]);
        }
        
        while(edgesintransition.size() > 0 || timesofar == 0){     
            //cout << edgesintransition.size() << " s "<< endl;
            // increment transit to travel by 1
            int edgesize = edgesintransition.size();
            vector<int> toerase;
            // for each edge in edgesintransition
            for(int i = 0; i < edgesize; i++){
                edgesintransition[i]->time -= 1;
                // reached node
                if(edgesintransition[i]->time <= 0){
                    int targetnode = edgesintransition[i]->target;
                    //cout << edgesintransition.size() << " size and i: " << i << endl;
                    // remove it after it is done traversing edge
                    toerase.emplace_back(i);
                    // add the children of this node to the edges in transition, if haven't reached it yet
                    //cout << "reached " << targetnode << endl;
                    //cout << reached.size() << endl;
                    if(reached.find(targetnode) == reached.end() || reached[targetnode] != 1){
                        //cout << "add " << targetnode << " edges" << endl;
                        for(int j = 0; j < nodes[targetnode].size(); j++){
                            //cout << "added edge from " << targetnode << endl;
                            edgesintransition.emplace_back(nodes[targetnode][j]);
                        }
                    }
                    reached[targetnode] = 1;
                }
            }
            // erase from back to front
            for(int k = toerase.size()-1; k > -1; k--){
                //cout << "erase " << toerase[k] << endl;
                edgesintransition.erase(edgesintransition.begin() + toerase[k]);
            }
            timesofar++;
            //cout << timesofar << " time now" << endl;
            // check if done
            bool done = checkDone();
            if(done){
                time = timesofar;
                return;
            }
        }
    }
    
    int networkDelayTime(vector<vector<int>>& times, int N, int K) {
        reached.clear();
        nodes.clear();
        edgesintransition.clear();
        time = 0;
        num = N;
        // makes nodes from edges
        for(int i = 0; i < times.size(); i++){
            int source = times[i][0];
            int target = times[i][1];
            int time = times[i][2];
            Edge *ed = new Edge(source, target, time);
            nodes[source].emplace_back(ed);
        }
        // Send from K
        sendSig(K);
        
        bool done = checkDone();
        if(done){
            return time;
        } else {
            return -1;
        }
        // done
        return time;
    }
};