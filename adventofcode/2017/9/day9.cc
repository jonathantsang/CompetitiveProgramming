#include <bits/stdc++.h>
using namespace std;

vector<string> input;
map<string, int> dict;
int total = 0;

int i = 0;

int gothrough(string word, int j){
	bool garbage = false; //garbage
	bool exlm = false; // look until last >
	int left = 0;
	int right = 0;
	int score = 0;
	// each char
	for(i = j; i < word.length(); i++){
		if(word[i] == '>'){
			garbage = false;
		}
		if(word[i] == '!'){
			i++; // skip next char
			cout << "skip " << word[i] << endl;
		}
		if(garbage){ // meaning garbage
			// do nothing
		}
		else if(word[i] == '<'){
			garbage = true;
		}

		// braces
		else if(word[i] == '{'){
			int localscore = gothrough(word, i+1);
			cout << localscore + 1 << " got" << endl;
			total += localscore + 1;
			score += localscore + 1;

		}
		else if(word[i] == '}'){
			cout << "send " << score << endl;
			return score;
		}
	}
	return score;
}

int main(){
	string word = "";
	string all = "";
	while(cin >> word){
		all += word;
	}
	gothrough(all, 0);
	cout << total << " all" << endl;
}
