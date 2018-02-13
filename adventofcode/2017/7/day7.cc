#include <vector>
#include <sstream>
#include <map>
#include <iostream>
using namespace std;


// you can kind of cheese making the tree by assuming the root only appears once, all leaves appear
// as children somewhere else
int main(){
	map<string, int> dict;
	string line;
	while(getline(cin, line)){
		stringstream ss{line};
		string word;
		ss >> word;
		cout << word << endl;
		if(isalpha(!word[0])){
			continue;
		} else {
			if(dict.find(word) == dict.end()){
				dict[word] = 1;
			} else {
				dict[word] += 1;
			}
		}

		// -> words
		string a;
		string b;
		// (num) -> arrow trash
		if(ss >> a >> b){
			while(ss >> word){
				if(isalpha(!word[0])){
					continue;
				} else {
					// comma removal trauma center style
					if(word[word.length()-1] == ','){
						word = word.substr(0,word.length()-1);
						cout << word << " w" << endl;
					}
					if(dict.find(word) == dict.end()){
						dict[word] = 1;
					} else {
						dict[word] += 1;
					}
				}
			}
		}
	}
	// find only one
	for (auto it = dict.begin(); it != dict.end(); it++)
	{
		if(it->second == 1){
			cout << "f " << it->first << endl;
		}
	}
    
}
