#include <bits/stdc++.h>
using namespace std;

int main(){
	string nums;
	getline(cin, nums);
	istringstream iss{nums};
	int withdraw;
	float bankamt;
	iss >> withdraw >> bankamt;
	if(withdraw % 5 != 0){
	} else if (withdraw > bankamt){
	} else if (bankamt - 0.5 < withdraw) {
	} else {
		// Valid
		bankamt -= 0.5;
		bankamt -= withdraw;
	}
	cout << fixed;
    cout << setprecision(2);
	cout << bankamt << endl;
	
}