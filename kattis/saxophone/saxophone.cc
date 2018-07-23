#include <bits/stdc++.h>
using namespace std;

map<char, vector<int>> combo;

void keysPressed(string notes){//            
	int keys = 0; // binary format 00000000000
	//                            109876543210
	map<int, int> presses;
	presses[1] = 0;
	presses[2] = 0;
	presses[3] = 0;
	presses[4] = 0;
	presses[5] = 0;
	presses[6] = 0;
	presses[7] = 0;
	presses[8] = 0;
	presses[9] = 0;
	presses[10] = 0;

	for(int i = 0; i < notes.length(); i++){
		map<int, int> neededKeys;

		vector<int> pressed = combo[notes[i]];
		for(int j = 0; j < pressed.size(); j++){
			neededKeys[pressed[j]] = 1;

			if (((keys >> pressed[j]) & 1) == 1){
				// no new key press
			} else {
				// Need a key press at pressed[j]
				presses[pressed[j]]++;
			}
			// Set the key one regardless
			keys = (keys | (1 << pressed[j]));
		}

		// Go through from 1 to 10 for NON pressed ones
		for(int j = 1; j <= 10; j++){
			if(neededKeys.count(j) == 0){

				// Set the key one off
				keys &= ~(1 << j);
			}
		}
	}

	// Then print out presses
	int i = 0;
	for(auto p : presses){
		if(i + 1 == presses.size()){
			cout << p.second << endl;
			break;
		} else {
			cout << p.second << " ";
			i++;
		}
	}
}

int main() {

	vector<int> c{2,3,4,7,8,9,10};
	vector<int> d{2,3,4,7,8,9};
	vector<int> e{2,3,4,7,8};
	vector<int> f{2,3,4,7};
	vector<int> g{2,3,4};
	vector<int> a{2,3};
	vector<int> b{2};
	vector<int> C{3};
	vector<int> D{1,2,3,4,7,8,9};
	vector<int> E{1,2,3,4,7,8};
	vector<int> F{1,2,3,4,7};
	vector<int> G{1,2,3,4};
	vector<int> A{1,2,3};
	vector<int> B{1,2};

	combo['c'] = c;
	combo['d'] = d;
	combo['e'] = e;
	combo['f'] = f;
	combo['g'] = g;
	combo['a'] = a;
	combo['b'] = b;
	combo['C'] = C;
	combo['D'] = D;
	combo['E'] = E;
	combo['F'] = F;
	combo['G'] = G;
	combo['A'] = A;
	combo['B'] = B;

	int cases;
	string line;
	cin >> cases;
	getline(cin, line);
	for(int i = 0; i < cases; i++){
		getline(cin, line);
		keysPressed(line);
	}
}