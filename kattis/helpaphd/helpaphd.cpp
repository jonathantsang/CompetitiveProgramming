#include <bits/stdc++.h>
using namespace std;

int main(){
	string line;
	getline(cin, line);
	istringstream iss{line};
	int cases;
	iss >> cases;
	for(int i = 0; i < cases; i++){
		getline(cin, line);
		if(line == "P=NP"){
			cout << "skipped" << endl;
		} else {
			istringstream is{line};
			int a;
			int b;
			is >> a >> b;
			cout << a + b << endl;
		}
	}
}