#include <bits/stdc++.h>
using namespace std;

int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	string name;
	cin >> name;
	string final = "";
	for(char c : name){
		if(c >= 'A' && c <= 'Z'){
			final += c;
		}
	}
	cout << final << endl;
}