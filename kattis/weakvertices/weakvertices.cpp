#include <bits/stdc++.h>
using namespace std;

map<int, int> type; // 0 is weak, 1 is strong
vector<vector<int>> adj;

int main(){
	int numvert;
	string val;
	while(cin >> numvert){
		if(numvert == -1){
			exit(0);
		}
		adj.clear();
		adj.resize(numvert);
		type.clear();
		for(int i = 0; i < numvert; i++){
			adj[i].resize(numvert);
			type[i] = 0;
		}
		string line;
		getline(cin, line);
		// Each line of input
		for(int i = 0; i < numvert; i++){
			getline(cin, line);
			istringstream iss{line};
			for(int j = 0; j < numvert; j++){
				iss >> adj[i][j];
				// cout << adj[i][j] << " ";
			}
			// cout << endl;
		}
		// cout << endl;

		// Then check for each vertice
		for(int i = 0; i < numvert; i++){
			if(type[i] == 1){
				continue; // skip
			}
			// For each neighbour of i
			for(int j = 0; j < numvert; j++){
				if(adj[i][j] != 1){
					continue;
				}
				if(i == j){
					continue;
				}
				// For each neighbour of j
				for(int k = 0; k < numvert; k++){
					if(adj[j][k] != 1){
						continue; // only check neighbours
					}
					if(i == k || j == k){
						continue;
					}
					// Check if it connected to i
					if(adj[i][k] == 1){
						// cout << "f" << endl;
						// Mark all i,j,k are strong
						type[i] = 1;
						type[j] = 1;
						type[k] = 1;
						// cout << i << " " << j << " " << k << endl;
					}
				}
			}
		}
		// Return all weak
		vector<int> weak;
		for(map<int,int>::iterator it = type.begin(); it != type.end(); ++it){
			if (type[it->first] == 0){
				weak.push_back(it->first);
			}
		}
		sort(weak.begin(), weak.end());
		for(int i = 0; i < weak.size(); i++){
			if(i + 1 == weak.size()){
				cout << weak[i];
			} else {
				cout << weak[i] << " ";
			}
		}
		cout << endl;
	}
}