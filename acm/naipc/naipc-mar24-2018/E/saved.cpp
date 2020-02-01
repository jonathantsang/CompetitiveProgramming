#include <bits/stdc++.h>
using namespace std;

int chosen = 1;

void makeVal(int n, int k){
	for(int i = 0; i < k; i++){
		chosen *= (n);
		n--;
	}
}

int main(){

	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	string line;

	while(getline(cin, line)){
		list<string> strings;

		istringstream iss{line};
		int n;
		int k;
		iss >> n >> k;
		for(int i = 0; i < n; i++){
			getline(cin, line);
			strings.push_back(line);
		}

		// sort strings
		strings.sort();

		// Make a map to tell instantly what order
		map<string, int> strings_order;
		int counter = 0;
		for(string s : strings){
			strings_order[s] = counter;
			counter++;
		}

		getline(cin, line);
		string word;
		word = line;

		double order = 0; // place so far, indexed at 1 modulo 10^9 + 7
		int n_val = n;
		int k_val = k;
		string word_val = word;
		map<string, int> used; // Can't repeat strings

		// makes chosen
		makeVal(n_val-1, k_val-1);

		while(k_val > 0){
			// Want to find largest string it is larger than
			string closest;
			bool prefix = false;
			int old_order = order;
			//int chosen = nChoosek(n_val-1, k_val-1) * factorial(k_val-1); // choosing with unique k-1!
			// chosen is n-1 * n-2 * n-3, k-1 times
			if(k != k_val){
				chosen /= n_val;
			}

			int num_counted = 0;
			// cout << "chosen factorial val " << chosen << endl;
			for(string s : strings){
				// if exact prefix choose that
				// Check if the char is valid to count up the num_counted
				if(used.find(s) != used.end()){
					continue; // skip the word since it is already used
				}

				// cout << "prefix " << word.substr(0, strings[j].length()) << endl;
				if(s == word_val.substr(0, s.length())){
					closest = s;
					// cout << num_counted << " num counterd" << endl;
					order = old_order + num_counted * chosen;
					prefix = true;

					// Final one
					if(k_val == 1 && s == word_val){
						order = old_order + (num_counted+1) * chosen; // One more for exact?
					}
					break; // since it is exact
				}
				// Check if the char is valid to count up the num_counted
				if(used.find(s) == used.end()){
					num_counted++;
				}
			}

			if(order >= (10e9 + 7)){
				double modulo = 10e9+7;
				order = fmod(order, modulo);
			}

			// add to used so it doesn't count it
			used[closest] = 1;
			n_val--;
			k_val--;
			word_val.erase(0, closest.length());
		}
		cout << order << endl;
	}
}