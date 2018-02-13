#include <iostream>
#include <vector>
#include <math.h>
using namespace std;

void printGrid(vector<vector<int>> &grid){
	for(int i = 0; i < grid.size(); i++){
		for(int j = 0; j < grid[i].size(); j++){
			cout << grid[i][j] << " ";
		}
		cout << endl;
	}
	cout << endl;
}

int checkNeighbours(vector<vector<int>> &grid, int x, int y){
	// square
	int h = grid.size();
	int w = grid[0].size();
	int total = 0;	

	// check square neighbours
	// N
	if(y-1 >= 0 && x){
		total += grid[y-1][x];
	}
	// NE
	if(y-1 >= 0 && x+1 >= 0){
		total += grid[y-1][x+1];
	}
	// E
	if(y && x+1 < w){
		total += grid[y][x+1];
	}
	// SE
	if(y+1 < h && x+1 < w){
		total += grid[y+1][x+1];
	}
	// S
	if(y+1 < h && x){
		total += grid[y+1][x];
	}
	// SW
	if(y+1 < h && x-1 >= 0){
		total += grid[y+1][x-1];
	}
	// W
	if(y && x-1 >=0){
		total += grid[y][x-1];
	}
	// NW
	if(y-1 >=0 && x-1 >=0){
		total += grid[y-1][x-1];
	}

	if(total > 361527){
		cout << total << " larger" << endl;
		exit(1);		
	}
	return total;
}

int makeSpiral(int num){
	int n = 1;
	vector<vector<int>> grid;	

	// largest odd square
	while(pow(n, 2) < num){
		n += 2;
	}
	cout << n << " " << pow(n,2) << endl;
	
	// new rows and columns
	for(int i = 0; i < n ; i++){
		vector<int> row;
		row.resize(n);
		grid.emplace_back(row);
	}
	int start = n / 2;
	grid[start][start] = 1;
	int x = start;
	int y = start;
	int savex = 0;
	int savey = 0;
	// construct spiral
	int sideL = 3;
	int i = 2;
	bool done = true; // done is when the perfect square has been place and needs to go right one
	// while i is not 
	while(i < num){
		if(done){ // a perfect square is formed
			x++;
			grid[y][x] = checkNeighbours(grid, x, y);
			if(i == num){
				savex = x;
				savey = y;
			}
			i++;
			done = false;
		} else {
			// perform 4 sides: sideL-1, sideL, sideL, sideL
			// right side, always one less
			for(int p = 0; p < sideL -1 - 1; p++){
				y--;
				grid[y][x] = checkNeighbours(grid, x, y);;
				i++;
			}
			// top
            for(int p = 0; p < sideL - 1; p++){
            	x--;
                grid[y][x] = checkNeighbours(grid, x, y);
                i++;
            }
			// left side
            for(int p = 0; p < sideL - 1; p++){
                y++;
               	grid[y][x] = checkNeighbours(grid, x, y);
                i++;
            }
			// bottom
            for(int p = 0; p < sideL - 1; p++){
                x++;
                grid[y][x] = checkNeighbours(grid, x, y);
                i++;
            }
			sideL += 2;
			done = true;
		}
	}
	printGrid(grid);
	return 1;;
}

int main(){
	int input = 361527;
	//int distance = makeSpiral(25);
	int distance = makeSpiral(361527);
	//cout << "dist: " << distance << endl;
	//return distance;
}
