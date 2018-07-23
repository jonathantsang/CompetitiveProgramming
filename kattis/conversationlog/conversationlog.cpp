#include <bits/stdc++.h>
using namespace std;

bool cust(const pair<int, string>& a, const pair<int, string>& b)

{
	if(a.first == b.first) return (a.second < b.second);
    return a.first > b.first;
}

int main(){
	map<string, int> totalCount; // total count overall
	map<string, set<string>> perPerson; // words incremented only by person
	map<string, int> seen; // how many times seen, once per person
	set<string> people;
	int n;
	cin >> n;
	string line;
	getline(cin, line);
	while(n--){
		getline(cin, line);
		istringstream iss{line};
		string word;
		string name;
		iss >> name; // Name
		people.insert(name);
		while(iss >> word){
			// Total count
			if(totalCount.count(word) == 0){
				totalCount[word] = 1;
			} else {
				totalCount[word]++;
			}

			// Person check if it has already been counted
			if(perPerson[name].count(word) == 0){
				perPerson[name].insert(word);
				if(seen.count(word) == 0){
					seen[word] = 1;
				} else {
					seen[word]++;
				}
			}
			// else already seen
		}
	}
	// After all words from people
	// Everything in perPerson with count of n is in all of the people
	vector<pair<int, string>> words;
	for(auto entry : seen){
		if(entry.second == people.size()){
			pair<int, string> group;
			group.first = totalCount[entry.first];
			// cout << entry.first << " " << group.first << endl;
			group.second = entry.first;
			words.push_back(group);
		}
	}

	if(words.size() == 0){
		cout << "ALL CLEAR" << endl;
	}

	// Sort by the first then second
	sort(words.begin(), words.end(), cust);

	for(pair<int, string> p : words){
		cout << p.second << endl;
	}



}