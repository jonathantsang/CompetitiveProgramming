#include <bits/stdc++.h>
using namespace std;

void print(vector<vector<int>> &g){
	for(vector<int> row : g){
		for(int v : row){
			cout << v;
		}
		cout << endl;
	}
}

int main(){
	string line;
	while(getline(cin, line)){
		vector<char> row_p;
		vector<char> col_p;

		int row_count = 0;
		int col_count = 0;
		
		// row parities
		for(int i = 0; i < line.length(); i++){
			if(line[i] == '1'){
				row_count++;
			}
			row_p.push_back(line[i]);
		}

		// get column parities
		getline(cin, line);
		for(int i = 0; i < line.length(); i++){
			if(line[i] == '1'){
				col_count++;
			}
			col_p.push_back(line[i]);
		}

		if(row_count != col_count){
			cout << "-1" << endl;
		} else {
			vector<vector<int>> grid;
			grid.resize(row_p.size());
			for(int i = 0; i < grid.size(); i++){
				grid[i].resize(col_p.size());
				fill(grid[i].begin(), grid[i].end(), 1);
			}
			// print(grid);
			
			// Need pairs of cols and rows with 1
			// start furthest left and up for 0s
			// Not at end for both
			int row = 0;
			int col = 0;
			while(row < row_p.size() && col < col_p.size()){
				// cout << row << " " << col << endl;
				// Find next 1 row
				while(row < row_p.size() && row_p[row] != '1'){
					row++;
				}

				// Find next 1 column
				while(col < col_p.size() && col_p[col] != '1'){
					col++;
				}

				// End
				if(col_p[col] != '1' || row_p[row] != '1'){
					break;
				}

				// Now at the furthest left and furthest right
				// Set to 0
				grid[row][col] = 0;

				row++;
				col++;
			}

			print(grid);
		}
	}

}