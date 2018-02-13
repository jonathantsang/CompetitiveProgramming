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
			grid[y][x] = i;
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
				grid[y][x] = i;
				if(i == num){
           	    	savex = x;
              		savey = y;
            	}
				i++;
			}
			// top
            for(int p = 0; p < sideL - 1; p++){
            	x--;
                grid[y][x] = i;
				if(i == num){
        	        savex = x;
    	            savey = y;
	            }
                i++;
            }
			// left side
            for(int p = 0; p < sideL - 1; p++){
                y++;
                grid[y][x] = i;
				if(i == num){
	                savex = x;
    	            savey = y;
        	    }
                i++;
            }
			// bottom
            for(int p = 0; p < sideL - 1; p++){
                x++;
                grid[y][x] = i;
				if(i == num){
                    savex = x;
                    savey = y;
                }
                i++;
            }
			sideL += 2;
			done = true;
		}
	}
	printGrid(grid);
	int dist = abs(start - savey) + abs(start - savex);
	return dist;
}

int main(){
	int input = 361527;
	int distance = makeSpiral(input);
	//int distance = makeSpiral(361527);
	cout << "dist: " << distance << endl;
	return distance;
}
