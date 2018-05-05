#include <bits/stdc++.h>
using namespace std;

int main(){
	int cases;
	string s;
	cin >> cases;
	getline(cin, s);
	for(int i = 0; i < cases; i++){
		int imported = 0;
		string nums;
		// For each number in the row
		getline(cin, nums);
		istringstream iss{nums};
		int previous = -1;
		int number = -1;
		while(iss >> number){
			if(number == 0){
				break; // end
			} else if(previous == -1){
				// skip
			} else {
				// check if x2 previous compared to now
				if(previous * 2 < number){
					imported += (number - previous * 2);
				}
			}
			previous = number;
		}
		cout << imported << endl;
	}
}