#include <bits/stdc++.h>
using namespace std;

int main(){
	int len;
	string word;
	cin >> len >> word;
	bool valid = true;
	bool hasquestionmark = false;
	char before_q = '1';
	bool questionblock = false;
	int question_len = 0;
	int permutation = 1;
	for(int i = 0; i < len; i++){
		if(questionblock && word[i] == '?'){
			question_len++;
		} else if (questionblock && word[i] != '?'){
			// End of block
			questionblock = false;
			// cout << "check " << before_q << " and " << word[i] << endl;
			if(question_len == 2){
				if(before_q == '1'){
					// Beginning it is fine, or reset value
					permutation *= 2;
				}
				// Check front and end
				else if(before_q == word[i]){
					// Can do it since C??C
					// valid = true;
					permutation *= 2;
				}
			} else {
				// works regardless
				permutation *= 2;
			}
			before_q = '1';
		}
		else if(word[i] == '?'){
			if(i == 0){
				// It is start
				before_q = '1';
			} else {
				before_q = word[i-1];
			}
			hasquestionmark = true;
			questionblock = true;
			question_len = 1;
		}
	}
	// Still has ??? block at end
	if(questionblock){
		permutation *= 2;
	}
	if(!hasquestionmark){
		cout << "No" << endl;
		exit(0);
	}
	// Go to end for ?? block, it must be valid
	if(permutation == 1){
		cout << "No" << endl;
	} else {
		cout << "Yes" << endl;
	}
}