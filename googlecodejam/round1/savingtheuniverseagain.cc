#include <bits/stdc++.h>
using namespace std;

int execute(string &seq){
	int total = 0;
	int dmg = 1;
	for(int i = 0; i < seq.length(); i++){
		if(seq[i] == 'C'){
			dmg *= 2;
		} else if (seq[i] == 'S'){
			total += dmg;
		}
	}
	return total;
}

void replace(string &s, int index){
	s[index] = 'S';
	s[index+1] = 'C';
}

int findLastCS(string &s){
	for(int i = s.length()-2; i >= 0; i--){
		if(s[i] == 'C' && s[i+1] == 'S'){
			return i;
		}
	}
	return 0;
}

int main(){
	int cases;
	string line;
	cin >> cases;
	getline(cin, line);
	for(int i = 0; i < cases; i++){
		int swaps = 0;

		getline(cin, line);
		istringstream iss{line};
		int shield;
		string sequence;
		iss >> shield >> sequence;

		// For each one count up S to see if impossible
		int s = 0;
		int c = 0;
		for(int i = 0; i < sequence.length(); i++){
			if(sequence[i] == 'C'){
				c++;
			} else if (sequence[i] == 'S'){
				s++;
			}
		}
		// IMPOSSIBLE
		if(s > shield){
			cout << "Case #" << i+1 << ": " << "IMPOSSIBLE" << endl;
			continue;
		} else {
			// POSSIBLE
			int value = execute(sequence);
			// cout << value << endl;
			// already possible
			if(value < shield){
				swaps = 0;
				cout << "Case #" << i+1 << ": " << swaps << endl;
				continue;
			} else {
				// Need some swaps
				while(value > shield){
					// try to do the latest "cs" swap
					int found = findLastCS(sequence);
					// cout << "found " << found << endl;
					replace(sequence, found);
					// cout << "new sequence " << sequence << endl;
					value = execute(sequence);
					swaps++;
				}
				cout << "Case #" << i+1 << ": " << swaps << endl;
			}
		}
	}
}