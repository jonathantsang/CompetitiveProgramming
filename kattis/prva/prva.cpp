#include <bits/stdc++.h>
using namespace std;

int main() {
	vector<vector<char>> grid;
	vector<string> words;
	string line;
	getline(cin, line);
	int height;
	int width;
	istringstream iss{line};
	iss >> height >> width;

	for(int i = 0; i < height; i++){
		getline(cin, line);
		vector<char> row;
		for(int j = 0; j < line.length(); j++){
			row.push_back(line[j]);
		}
		grid.push_back(row);
	}

	// have the grid now, form the words horizontally
	for(int i = 0; i < height; i++){
		string formed = "";
		for(int j = 0; j < width; j++){
			if(grid[i][j] == '#'){
				if(formed.length() > 1){
					words.push_back(formed);
				}
				formed = "";
			} else {
				formed += grid[i][j];
			}
		}
		// Add formed to strings
		if(formed.length() > 1){
			words.push_back(formed);
		}
	}

	// words vertically
	for(int i = 0; i < width; i++){
		string formed = "";
		for(int j = 0; j < height; j++){
			if(grid[j][i] == '#'){
				if(formed.length() > 1){
					words.push_back(formed);
				}
				formed = "";
			} else {
				formed += grid[j][i];
			}
		}
		// Add formed to strings
		if(formed.length() > 1){
			words.push_back(formed);
		}
	}

	// sort the words
	sort(words.begin(), words.end());

	cout << words[0] << endl;
}