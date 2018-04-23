#include <bits/stdc++.h>
using namespace std;

int main(){
	int cases;
	string line;
	cin >> cases;
	getline(cin, line);
	for(int c = 0; c < cases; c++){
		int len;
		cin >> len;
		getline(cin, line);

		// Get numbers
		getline(cin, line);
		istringstream iss{line};
		vector<int> evens;
		vector<int> odds;
		for(int i = 0; i < len; i++){
			int val;
			iss >> val;
			if(i % 2 == 0){
				evens.push_back(val);
			} else {
				odds.push_back(val);
			}
		}
		// Find if it will sort it correctly

		// sort first
		sort(evens.begin(), evens.end());
		sort(odds.begin(), odds.end());

		bool valid = true;
		// Evens start and each value alternating must be great than the value it had previous
		int ep = 0;
		int op = 0;
		int count = 0; // how many checks "index"
		while(ep < evens.size() && op < odds.size()){
			if(ep == op){
				// cout << evens[ep] << " " << odds[op] << endl;
				if(odds[op] >= evens[ep]){
					// good
				} else {
					cout << "Case #" << c+1 << ": " << count << endl;
					valid = false;
					break;
				}
				ep++;
			} else {
				// cout << evens[ep] << " " << odds[op] << endl;
				if(evens[ep] >= odds[op]){
					// good
				} else {
					cout << "Case #" << c+1 << ": " << count << endl;
					valid = false;
					break;
				}
				op++;
			}
			count++;
		}
		if(valid){
			cout << "Case #" << c+1 << ": " << "OK" << endl;
		}
	}
}