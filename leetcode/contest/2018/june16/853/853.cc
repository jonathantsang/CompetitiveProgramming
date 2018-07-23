class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        if(position.empty()){
            return 0;
        }
        if(position.size() == 1){
            return 1;
        }
        int fleets = 0;
        vector<pair<int,int>> cars;
        for(int i = 0; i < position.size(); i++){
            pair<int, int> p;
            p.first = position[i];
            p.second = speed[i];
            cars.push_back(p);
        }
        
        // sort by first element, position
        sort(cars.begin(), cars.end());
        
        int previous = (target - cars[0].first) / cars[0].second;
        previous = (target - cars[0].first) % cars[0].second != 0 ? previous + 1 : previous;
        
        vector<float> times;
        for(int i = 0; i < cars.size(); i++){
            float timetoarrive = (float) (target - cars[i].first) / (float) cars[i].second;
            // timetoarrive = (target - cars[i].first) % cars[i].second != 0 ? timetoarrive + 1 : timetoarrive;
            times.push_back(timetoarrive);
            // cout << timetoarrive << endl;
        }
                
        // Then go backwards finding backlog
        float backlog = times.back();
        for(int i = times.size()-2 ; i >= 0; i--){
            if(times[i] > backlog){
                // cout << times[i] << " < " << backlog << endl; 
                // not the slowest anymore
                fleets++; // the gap
                backlog = times[i];
            } else {
                // slowed down by backlog still
            }
        }
        // last one is a fleet
        fleets++;
        return fleets;
    }
};