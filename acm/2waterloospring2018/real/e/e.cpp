#include <bits/stdc++.h>
using namespace std;

map<char, int> lookup;
map<string, int> seen;

int main(){
	lookup['A'] = 2;
	lookup['B'] = 2;
	lookup['C'] = 2;
	lookup['D'] = 3;
	lookup['E'] = 3;
	lookup['F'] = 3;
	lookup['G'] = 4;
	lookup['H'] = 4;
	lookup['I'] = 4;
	lookup['J'] = 5;
	lookup['K'] = 5;
	lookup['L'] = 5;
	lookup['M'] = 6;
	lookup['N'] = 6;
	lookup['O'] = 6;
	lookup['P'] = 7;
	lookup['R'] = 7;
	lookup['S'] = 7;
	lookup['T'] = 8;
	lookup['U'] = 8;
	lookup['V'] = 8;
	lookup['W'] = 9;
	lookup['X'] = 9;
	lookup['Y'] = 9;
	int amt = 0;
	cin >> amt;
	string line;
	getline(cin, line);
	for(int i = 0; i < amt; i++){
		getline(cin, line);
		// cout << line << endl;
		string number;
		for(int i = 0; i < line.length(); i++){
			if(line[i] != '-'){
				if(line[i] >= 'A' && line[i] <= 'Z'){
					string a = to_string(lookup[line[i]]);
					number += a;
				} else {
					number += line[i];
				}
			}
		}
		// cout << number << endl;
		if(seen.count(number) > 0){
			seen[number]++;
		} else {
			seen[number] = 1;
		}
	}
	// Find duplicates
	vector<string> dupes;
	map<string, int> count;

	for(map<string, int>::iterator it = seen.begin(); it != seen.end(); it++){
		if(it->second > 1){
			string num = it->first;
			string val = num.substr(0,3) + '-' + num.substr(3);
			dupes.push_back(val);
			count[val] = it->second;
		}
	}
	if(dupes.size() == false){
		cout << "No duplicates." << endl;
	} else {
		sort(dupes.begin(), dupes.end());
		for(int i = 0; i < dupes.size(); i++){
			cout << dupes[i] << " " << count[dupes[i]] << endl;
		}
	}
}