#include <bits/stdc++.h>
using namespace std;

int main(){
	string line;
	while(getline(cin, line)){
		istringstream iss{line};
		int n; // original
		int trick;
		iss >> n >> trick;

		map<int, int> seen; // what we have
		vector<int> vals;
		for(int i = 0; i < trick; i++){
			int get;
			getline(cin, line);
			istringstream is{line};
			is >> get;
			vals.push_back(get);
			seen[get] = 1;
		}

		// Go through lowest missing from 1 to n
		int highest_added = 1;
		for(int i = 0; i < vals.size(); i++){
			// for each val input, start from highest, and try to add all not in seen
			for(int j = highest_added; j < vals[i]; j++){
				if(seen.find(j) == seen.end()){
					// Not in seen, was removed
					cout << j << endl;
					seen[j] = 1; // add to the seen
				} else {
					// Don't do anything, just increment
				}
			}
			highest_added = max(highest_added, vals[i]);
			cout << vals[i] << endl; // At the end
		}
		// cout << highest_added << endl;
		if(highest_added < n){
			// At the end go from highest_added to n
			for(int i = highest_added+1; i <= n; i++){
				cout << i << endl;
			}
		}
	}
}