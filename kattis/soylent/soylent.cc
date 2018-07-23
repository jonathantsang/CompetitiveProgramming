#include <bits/stdc++.h>
using namespace std;

int main() {
	int cases;
	cin >> cases;
	for(int i = 0; i < cases; i++){
		int calories;
		cin >> calories;
		int bottles = calories / 400;
		bottles = calories % 400 == 0 ? bottles : bottles+1;
		cout << bottles << endl;
	}
}