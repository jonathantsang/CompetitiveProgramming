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

		int maxstrlen = 0;
		for(int i = 0; i < n; i++){
			getline(cin, line);
			strings.push_back(line);
			maxstrlen = maxstrlen > line.length() ? maxstrlen : line.length();
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
		map<int, int> used; // Can't repeat strings, for every int smaller, minus 1 to num_counted

		// makes chosen
		makeVal(n_val-1, k_val-1);

		while(k_val > 0){
			// Want to find largest string it is larger than
			string closest;
			int old_order = order;
			//int chosen = nChoosek(n_val-1, k_val-1) * factorial(k_val-1); // choosing with unique k-1!
			if(k != k_val){
				chosen /= n_val;
			}

			int num_counted = 0;
			int placement = 0;
			// cout << "word is " << word_val << endl;
			// cout << "chosen factorial val " << chosen << endl;
			for(int i = 1; i <= maxstrlen; i++){
				// cout << "check " << word_val.substr(0, i) << endl;
				if(strings_order.find(word_val.substr(0, i)) != strings_order.end()){
					closest = word_val.substr(0, i);
					// cout << "got word " << closest << endl;
					num_counted = strings_order[word_val.substr(0, i)];
					placement = strings_order[word_val.substr(0, i)];
					break;
				}
			}
			// cout << "placement is " << placement << endl;

			// go through used
			for(pair<int, int> p : used){
				if(p.first < placement){
					num_counted--;
					// cout << "dec" << endl;
				}
				// cout << "amt" << endl;
			}

			// cout << "cur order " << order << endl; 
			// cout << "prefix " << word.substr(0, strings[j].length()) << endl;
			// cout << num_counted << " num counted" << endl;
			order = old_order + num_counted * chosen;
			if(order >= (10e9 + 7)){
				double modulo = 10e9+7;
				order = fmod(order, modulo);
			}

			// Final one
			if(k_val == 1){
				order = old_order + (num_counted+1) * chosen; // One more for exact?
				if(order >= (10e9 + 7)){
					double modulo = 10e9+7;
					order = fmod(order, modulo);
				}
			}

			// add to used so it doesn't count it
			used[placement] = 1;
			n_val--;
			k_val--;
			word_val.erase(0, closest.length());
		}
		cout << order << endl;
	}
}