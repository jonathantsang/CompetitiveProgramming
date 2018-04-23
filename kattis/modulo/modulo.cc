#include <bits/stdc++.h>
using namespace std;

int main(){
	// mod 42
	map<int, int> counts;
	// read in 10
	int num;
	for(int i = 0; i < 10; i++){
		cin >> num;
		if(counts.find(num % 42) == counts.end()){
			counts[num % 42] = 1;
		} else {
			counts[num % 42]++;
		}
	}
	cout << counts.size() << endl;
}