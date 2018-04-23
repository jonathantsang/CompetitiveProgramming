#include <bits/stdc++.h>
using namespace std;

int main(){
	int len;
	string word;
	cin >> len >> word;
	vector<int> possible;
	possible.resize(len);
	fill(possible.begin(), possible.end(), 1);
	for(int i = 0; i < len; i++){
		if(i - 1 > -1 && word[i-1] == word[i] && word[i] != '?'){
			cout << "No" << endl;
			exit(0);
		} else if (i + 1 < len && word[i+1] == word[i] && word[i] != '?'){
			cout << "No" << endl;
			exit(0);
		}
		if(word[i] == '?'){
			// Check if it is length 1
			char before = '0';
			char after = '1';
			if(i - 1 > -1){
				before = word[i-1];
			}
			if(i + 1 < len){
				after = word[i+1];
			}
			if(before == '0' || after == '1'){
				// Beginning or end case
				possible[i] = 2;
			}
			else if(before != after && before != '?' && after != '?'){
				possible[i] = 1;
			} else {
				possible[i] = 2;
			}
		} else {
			// regular char
			possible[i] = 1;
		}
	}
	// End make sure it is all different and has multiple possibilities
	for(int i = 0; i < len; i++){
		if(possible[i] != 1){
			cout << "Yes" << endl;
			exit(0);
		}
	}
	cout << "No" << endl;
}