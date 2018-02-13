#include <vector>
#include <iostream>
using namespace std;


int traverse(vector<int> &jumps){
	int steps = 0;
	// can't be below bottom or above top
	int bottom = 0;
	int top = jumps.size() - 1;
	bool jumping = true;
	int index = 0;
	while(jumping){
		int jumpsize = jumps[index];
		jumps[index]++; // Increases by 1
		index += jumpsize;
		steps++;
		//cout << " go to " << index << endl;
		if(index < bottom || index > top){
			jumping = false;
			return steps;
		}
	}
	return steps;
}

int main(){
	vector<int> jumps;
	int num;
	while(cin >> num){
		jumps.emplace_back(num);
	}
	int steps = traverse(jumps);
	cout << "s " << steps << endl;
}
