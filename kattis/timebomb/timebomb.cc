#include <bits/stdc++.h>
using namespace std;

int num = 0;
vector<string> lines;

int number(int start, int len){
	// Read in lines from lines
	// and find the number
	/*
	cout << lines[0].substr(start, len) << endl;
	cout << lines[1].substr(start, len) << endl;
	cout << lines[2].substr(start, len) << endl;
	*/

	if(lines[0].substr(start, len) == "  *"){
		return 1;
	}
	else if(lines[0].substr(start, len) == "* *"){
		return 4;
	} else {
		// ***
		if(lines[1].substr(start, len) == "* *"){
			// 0, 8, 9
			if(lines[2].substr(start, len) == "* *"){
				return 0;
			} else {
				// 8, 9
				if(lines[3].substr(start, len) == "* *"){
					return 8;
				} else {
					return 9;
				}
			}
		}
		else if (lines[1].substr(start, len) == "  *"){
			// 2, 3, 7
			if(lines[2].substr(start, len) == "***"){
				// 2, 3
				if(lines[3].substr(start, len) == "*  "){
					return 2;
				} else {
					return 3;
				}
			} else {
				return 7;
			}
		}
		else if (lines[1].substr(start, len) == "*  "){
			// 5, 6
			if(lines[3].substr(start, len) == "* *"){
				return 6;
			} else {
				return 5;
			}
		}
	}
	return 0;
}

int main(){
	string line;
	
	while(getline(cin, line)){
		lines.push_back(line);
	}
	int start = 0;
	while(start < lines[0].size()){
		// check number from start to end
		num *= 10;
		int n = number(start, 3);
		// cout << n << endl;
		num += n;
		start += 4;
	}
	// cout << "n" << num << endl;
	if(num % 6 == 0){
		cout << "BEER!!" << endl;
	} else {
		cout << "BOOM!!" << endl;
	}
}