#include <bits/stdc++.h>
using namespace std;

int main(){
	int rows;
	int cols;
	string nums;
	getline(cin, nums);
	istringstream isn {nums};
	isn >> rows >> cols;
	string row;
	vector<vector<char>> opt;
	opt.resize(rows);
	for(int i = 0; i < rows; i++){
		opt[i].resize(cols);
	}
	int v = 0;
	int counter = 0;
	while(v < rows){
		getline(cin, row);
		for(int j = 0; j < row.length(); j++){
			opt[v][j] = row[j];
		}
		v++;
	}
	for(int i = 0; i < opt.size(); i++){
		for(int j = 0; j < opt[i].size(); j++){
			if(opt[i][j] == 'W'){
				bool valid = true;
				// Check if top, bottom, left, right are not sheep
				if(i-1 > -1){
					if(opt[i-1][j] == 'S'){
						valid = false;
						cout << "No" << endl;
						return 0;
					} else if (opt[i-1][j] == 'W'){
						// can't do anything to wolf
					} else if (opt[i-1][j] == '.'){
						opt[i-1][j] = 'D';
					}
				}
				if(i+1 < opt.size()){
					if(opt[i+1][j] == 'S'){
						valid = false;
						cout << "No" << endl;
						return 0;
					} else if (opt[i+1][j] == 'W'){
						// can't do anything to wolf
					} else if (opt[i+1][j] == '.'){
						opt[i+1][j] = 'D';
					}
				}
				if(j-1 > -1){
					if(opt[i][j-1] == 'S'){
						valid = false;
						cout << "No" << endl;
						return 0;
					} else if (opt[i][j-1] == 'W'){
						// can't do anything to wolf
					} else if (opt[i][j-1] == '.'){
						opt[i][j-1] = 'D';
					}
				}
				if(j+1 < opt[i].size()){
					if(opt[i][j+1] == 'S'){
						valid = false;
						cout << "No" << endl;
						return 0;
					} else if (opt[i][j+1] == 'W'){
						// can't do anything to wolf
					} else if (opt[i][j+1] == '.'){
						opt[i][j+1] = 'D';
					}
				}
				if(!valid){
					cout << "No" << endl;
					return 0;
				}
			}
		}
	}
	cout << "Yes" << endl;
	for(vector<char> r : opt){
		for(char c : r){
			cout << c;
		}
		cout << endl;
	}
	return 0;
}