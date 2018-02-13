#include <iostream>
#include <map>
#include <sstream>
using namespace std;



int main(){
	int valid = 0;
	string line;
	// each passphrase
	while(getline(cin, line)){
		bool good = true;
		map<string, int> dict;
		string word;
		stringstream ss{line};
		// add each word to dict
		while(ss >> word){
			if(dict.find(word) != dict.end()){
				good = false;
				break;
			}
			dict[word] = 1;
		}
		if(good){
			valid++;
		}
	}
	cout << valid << " v" << endl;
	return valid;
}
