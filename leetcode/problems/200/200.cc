class Solution {
    void print(vector<vector<int>>& grid){
        for(auto row : grid){
            for(auto val : row){
                cout << val << " ";
            }
            cout << endl;
        }
        cout << endl;
    }
public:
    int numIslands(vector<vector<char>>& grid) {
        if(grid.size() == 0){
            return 0;
        }
        map<pair<int,int>, int> convert; // which have been converted
        int a = grid.size();
        vector<vector<int>> mapv(a);
        for(int i = 0; i < mapv.size(); i++){
            mapv[i].resize(grid[0].size());
        }
        
        int counter = 1;
        int islands = 0;
        // print(mapv);
        for(int i = 0; i < grid.size(); i++){
            for(int j = 0; j < grid[i].size(); j++){
                if(grid[i][j] == '1'){
                    // do check if above or below
                    bool above = false;
                    bool left = false;
                    if(i-1 >= 0 && grid[i-1][j] == '1'){
                        above = true;
                    }
                    if(j-1 >= 0 && grid[i][j-1] == '1'){
                        left = true;
                    }
                    if(!left && !above){
                        // cout << "new island " << counter << " at " << i << " " << j << endl;
                        islands++;
                        mapv[i][j] = counter;
                        counter++;
                        // print(mapv);
                    }
                    
                    if(above){
                        mapv[i][j] = mapv[i-1][j];
                    }
                    if(left){
                        mapv[i][j] =  mapv[i][j-1];
                    }
                    
                    if(left && above){
                        // print(mapv);
                        // island mismatch is the same
                        if(mapv[i-1][j] != mapv[i][j-1]){
                            // cout << "different at " << i << " " << j << endl;
                            pair<int, int> same;
                            same.first = mapv[i-1][j];
                            same.second = mapv[i][j-1];
                            
                            pair<int, int> swap;
                            swap.first = mapv[i][j-1];
                            swap.second= mapv[i-1][j];
                            
                            if(convert.count(same) == 0 || convert.count(swap) == 0) {
                                islands--;
                                convert[same] = 1;
                                convert[swap] = 1;
                            }
                        }
                    }
                } else {
                    mapv[i][j] = 0;
                }   
            }
        }
        // print(mapv);
        return islands;
    }
};