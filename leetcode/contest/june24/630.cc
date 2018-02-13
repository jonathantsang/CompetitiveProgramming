class Solution {
public:
    int scheduleCourse(vector<vector<int>>& courses) {
        int timen = 0;
        int total = 0;
        bool notbust = true;
        vector<int> cantuse;
        while(notbust){
        int bestzero = 0;
        int bestnumpaths = 0;
        int bestnumpathchoice = -1;
            cout << "time is " << timen << endl;
            for(int i=0; i < courses.size(); i++){
                int numpaths = 0;
                bool skip = false;
                // Invalidate ones already chosen
                for(int p = 0; p < cantuse.size(); p++){
                    cout << cantuse[p]  << " can't use"<< endl;
                    if(i == cantuse[p]){
                       skip = true;
                    }
                }
                if(skip) { continue; }
                // Check for each choice, if it is run + time, which opens the most paths
                for(int j=0; j < courses.size(); j++){
                    bool bad = false;
                    // This makes it a valid choice later on with d
                    for(int p = 0; p < cantuse.size(); p++){
                        if(j == cantuse[p]){
                           bad = true;
                        }
                    }
                    if(j != i && !bad && timen + courses[j][0] < courses[j][1]){
                        cout << timen + courses[j][0] << " less than " << courses[j][1] << endl;
                        numpaths += 1;
                    }
                }
                cout << courses[i][0] << " val" << endl;
                cout << numpaths << endl;
                if(numpaths > bestnumpaths){
                    bestnumpaths = numpaths;
                    bestnumpathchoice = i;
                }
            }
            if(bestnumpathchoice == -1){
                return total;
            }
            cout << bestnumpathchoice << " best numpath" << endl;
            cantuse.push_back(bestnumpathchoice);
            // Allot time
            timen += courses[bestnumpathchoice][0];
            cout << timen << " new time" << endl;
            total += 1;
        }
    }
};