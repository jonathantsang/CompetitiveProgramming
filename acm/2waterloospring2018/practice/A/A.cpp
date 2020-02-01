#include <bits/stdc++.h>
using namespace std;

int main(){
	string line;
	while(getline(cin, line)){
		istringstream iss{line};
		int a;
		int b;
		int c;
		iss >> a >> b >> c;
		if(a == 0 && b == 0 && c == 0){
			break;
		}
		if(pow(a, 2) + pow(b, 2) == pow(c, 2)){
			cout << "right" << endl;
		} else if (pow(b, 2) + pow(c, 2) == pow(a,2)){
			cout << "right" << endl;
		} else if (pow(c, 2) + pow(a, 2) == pow(b, 2)){
			cout << "right" << endl;
		} else {
			cout << "wrong" << endl;
		}
	}
}