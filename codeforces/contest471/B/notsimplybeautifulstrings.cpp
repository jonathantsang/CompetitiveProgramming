#include <bits/stdc++.h>
using namespace std;

int main(){
	string word;
	cin >> word;
	map<char, int> counts;

	// Possible are 
	// 2 even, 1 odd
	// 2 even, 2 odd
	// 1 even, 1 odd
	for(int i = 0; i < word.length(); i++){
		if(counts.find(word[i]) == counts.end()){
			counts[word[i]] = 1;
		} else {
			counts[word[i]]++;
		}
	}
	// All the counts now
	int even = 0;
	int odd = 0;
	for(map<char, int>::iterator it = counts.begin(); it != counts.end(); it++){
		if(it->second % 2 == 0){
			even++;
		} else {
			odd++;
		}
	}
	// cout << "got even " << even << " got odd " << odd << endl; 
	if((even == 2 && odd == 1) || (even == 2 && odd == 2) || (even == 1 && odd == 1) || (odd == 2 && even == 1)
		|| (even == 2 && odd == 0) || (even == 0 && odd == 2) || (even == 4 && odd == 0) || (even == 3 && odd == 1) ||
		(even == 1 && odd == 3) || (even == 0 && odd == 4) || (even == 0 && odd == 3) || (even == 3 && odd == 0)){
		if(even == 1 && odd == 1){
			// Check the 2 leng even and 1 leng odd case
			int odd_count = 0;
			int even_count = 0;
			for(map<char, int>::iterator it = counts.begin(); it != counts.end(); it++){
				if(it->second % 2 == 0){
					even_count = it->second;
				} else {
					odd_count = it->second;
				}
			}
			if(odd_count == 1){
				cout << "No" << endl;
				return 0;
			}
		} else if (even == 0 && odd == 2){
			// Check that both odd are not leng 1
			bool fail = false;
			for(map<char, int>::iterator it = counts.begin(); it != counts.end(); it++){
				if(it->second % 2 == 1){
					if(it->second == 1){
						fail = true;
					}
				}
			}
			if(fail){
				cout << "No" << endl;
				return 0;
			}
		} else if (even == 0 && odd == 3){
			// Check that both odd are not leng 1
			bool fail = true;
			for(map<char, int>::iterator it = counts.begin(); it != counts.end(); it++){
				if(it->second % 2 == 1){
					if(it->second != 1){
						fail = false;
					}
				}
			}
			if(fail){
				cout << "No" << endl;
				return 0;
			}
		}
		cout << "Yes" << endl;
	} else {
		cout << "No" << endl;
	}
}