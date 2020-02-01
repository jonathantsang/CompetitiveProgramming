#include <bits/stdc++.h>
using namespace std;

string checkWord(string word, int place, int &numLetters, unordered_map<string, int> &words, unordered_map<int, vector<char>> &indicies){
	// cout << word << " place " << place << endl;
	if(place >= word.length()){
		return "-1";
	}
	// cout << word << endl;
	if(word.length() == numLetters && words.count(word) == 0){
		// word not in words
		return word;
	} else if (place == numLetters){
		// word in words
		return "-1"; // fail
	} else {
		// go through each letter making the new word at index place
		for(int i = 0; i < indicies[place].size(); i++){
			// replace character
			string old = word;
			word = word.substr(0,place) + indicies[place][i] + word.substr(place+1);
			if(words.count(word) == 0){
				return word;
			}
			// didn't work go deeper
			string s = checkWord(word, place+1, numLetters, words, indicies);
			if(s == "-1"){
				// fail on going deeper for this word
			} else {
				return s;
			}
			// revert
			word = old;
		}
		return "-1";
	}
}

int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int cases;
	cin >> cases;
	for(int i = 0; i < cases; i++){
		string newWord;

		long long numWords; // N
		int L; // L
		unordered_map<int, vector<char>> indicies;
		
		unordered_map<string, int> words;
		cin >> numWords >> L;

		string word;
		// for each of the words
		for(int j = 0; j < numWords; j++){
			unordered_map<char, int> letters;
			cin >> word;
			words[word] = 1;
			// for each char in the word
			for(int k = 0; k < word.length(); k++){
				// not in letters, add letter to indicies
				if(letters.count(word[k]) == 0){
					indicies[k].push_back(word[k]);
					letters[word[k]] = 1;
				}
			}
		}
		// letters has all letters
		// int numLetters = 0;
		//long long Permutations = pow(numLetters, L);

		// Check if it is in the permutations
		/*if(Permutations == numWords){
			// means it is full
			newWord = "-";
		} else {
			
		}*/

		// Check for each word, changing chars based on indices
		for(auto it = words.begin(); it != words.end(); ++it ){
			string word = it->first;
			string s = checkWord(word, 0, L, words, indicies); // has to have it
			if(s == "-1"){
				s = "-";
				newWord = s;
			} else {
				newWord = s;
				break;
			}	
		}
		cout << "Case #" << i+1 << ": " << newWord << endl;
	}
}