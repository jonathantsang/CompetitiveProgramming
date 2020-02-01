#include <bits/stdc++.h>
using namespace std;

int main(){
	string line;
	while(getline(cin, line)){
		if(line == "-"){
			break;
		}
		map<char, int> seen;
		for(int i = 0; i < line.length(); i++){
			if(line[i] >= 'A' && line[i] <= 'Z'){
				seen[line[i]] = 1;
			}
		}
		if(seen.size() == 26){
			cout << "Sufficient." << endl;
		} else {
			cout << "Deficient." << endl;
		}
	}
}