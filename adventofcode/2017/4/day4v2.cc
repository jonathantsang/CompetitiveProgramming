#include <iostream>
#include <map>
#include <sstream>
#include <algorithm>
using namespace std;


int wordSum(string word){
	int sum = 0;
	for (char ch : word)
	{
  		sum += ch;
	}
	return sum;
}

// Note: This didn't compile in C++11, but it will in C++14. I'm not sure what is wrong but it gives errors
// for my map that has a value of a vector. This gave the right answer still.
int main(){
	int valid = 0;
	string line;
	// each passphrase
	while(getline(cin, line)){
		bool good = true;
		map<int, vector<string>> dict;
		string word;
		stringstream ss{line};
		// add each word to dict
		while(ss >> word){
			int checksum = wordSum(word);
			int si = dict[checksum].size();
			if(si > 0){
				
				// go through each word to see if it is an anagram
				for(int i = 0; i < dict[checksum].size(); i++){
					// can be that they hash characters to the same, but not anagrams
                	sort(word.begin(), word.end());
                	sort(dict[checksum][i].begin(), dict[checksum][i].end());
	
					if(word == dict[checksum][i]){
						good = false;
						break;
					}
					
				}
				if(good == false){
					break;
				}
			}
			dict[checksum].emplace_back(word);
		}
		if(good){
			valid++;
		}
	}
	cout << valid << " v" << endl;
	return valid;
}
