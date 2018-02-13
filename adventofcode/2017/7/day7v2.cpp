#include <vector>
#include <sstream>
#include <map>
#include <iostream>
using namespace std;


// I did this without building the tree, I would recommend building the tree
// this solution works finds the answer. After some trial and error is done in mismatch correlation.
// vrgxe 1219 should fix it, my code just didn't know it failed a mismatch in the disk of a disk.
map<string, vector<string>>children;
map<string, int> dict;

// gets the total form the children recursively
int gettotal(string s){
	int balancet = 0;
	if(children.find(s) == children.end()){
		return dict[s]; // return self-value at least
	} 
	if(children[s].size() == 0){
			return dict[s];
	}
	else {
		// for each child
		int total= 0;
		vector<int> childsum;
		for(int i = 0; i < children[s].size(); i++){
			int amt = gettotal(children[s][i]);
			childsum.emplace_back(amt);
			total += amt;
		}
		// find mismatch
    	for(int k = 1; k < childsum.size(); k++){
    		if(childsum[k-1] != childsum[k]){
    			cout << childsum[k-1] << " " <<  childsum[k] << " diff " << endl;
                cout << children[s][k-1] << " " << children[s][k] << " c " << endl;
    			cout << s << " dea " << childsum[k-1] - childsum[k] + dict[s] << endl;
                exit(1);
    		}
    	}
		// done
		return dict[s] + total;
	}
}


int main(){
	vector<string> input;
	string line;
	while(getline(cin, line)){
		input.emplace_back(line);
		stringstream ss{line};
		string word;
		ss >> word;
		string weight;
		ss >> weight;
		// get num, rid of brackets
		istringstream iss{weight.substr(1,weight.length()-2)};
		int wei;
		iss >> wei;
		// all weights in dict now with weight
		dict[word] = wei;
    }

    for(int i = 0; i < input.size(); i++){
    	string node;
    	stringstream ss{input[i]};
    	ss >> node;
    	string num;
    	ss >> num;
    	string arrow;
    	string word;
    	if(ss >> arrow){
    		// each child
	    	while(ss >> word){
	    		// convert for comma
	    		if(word[word.length()-1] == ','){
	    			word = word.substr(0,word.length()-1);
	    		}
	    		cout << node << " has " << word << endl;
	    		children[node].emplace_back(word);
	    	}
    	}
    }

    // For each node check it is balanced among the children
    for(int i = 0; i < input.size(); i++){
    	string node;
    	stringstream ss{input[i]};
    	ss >> node;
    	string num;
    	ss >> num;
    	string arrow;
    	string word;
    	cout << node << endl;
    	int total = dict[node];
    	vector<int> childsum;
    	// for each child of the node
    	for(int j = 0; j < children[node].size(); j++){
    		int val = gettotal(children[node][j]);
    		cout << children[node][j] << " child has " << val << " v " << endl;
    		childsum.emplace_back(val);
    		total += val;
    	}
    	if(children[node].size() != 0 && total % children[node].size() != 0){
    		// find mismatch
    		for(int k = 1; k < childsum.size(); k++){
    			if(childsum[k-1] != childsum[k]){
    				cout << childsum[k-1] << " " <<  childsum[k] << " d " << endl;
    				cout << node << " dea " << childsum[k-1] - childsum[k] + dict[node] << endl;
                    exit(1);
    			}
    		}
    	}
    }
}
