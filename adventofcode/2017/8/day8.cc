#include <bits/stdc++.h>
using namespace std;


int main(){
	string line;
	map<string, int> registers;
	vector<string> input;
	// Set all registers
	while(getline(cin, line)){
		input.emplace_back(line);
		cout << line << endl;
		stringstream ss{line};
		string name;
		ss >> name;
		registers[name] = 0;
	}

	// input
	for(int i = 0; i < input.size(); i++){
		stringstream ss{input[i]};
		string word;
		string action; // dec or inc
		string num1;
		string ifs; // if statement
		string reg; 
		string op;
		string num2;
		ss >> word >> action >> num1 >> ifs >> reg >> op >> num2;
		istringstream iss1{num1};
		int num3;
		iss1 >> num3;
		istringstream iss2{num2};
		int num4;
		iss2 >> num4;

		// flip negative if decrease
		if(action == "dec"){
			num3 = -num3;
		}

		if(op == "<"){
			if(registers[reg] < num4){
				registers[word] += num3;
			}
		}
		else if(op == ">"){
			if(registers[reg] > num4){
				registers[word] += num3;
			}
		}
		else if(op == "<="){
			if(registers[reg] <= num4){
				registers[word] += num3;
			}
		}
		else if(op == ">="){
			if(registers[reg] >= num4){
				registers[word] += num3;
			}
		}
		else if(op == "=="){
			if(registers[reg] == num4){
				registers[word] += num3;
			}
		}
		else if(op == "!="){
			if(registers[reg] != num4){
				registers[word] += num3;
			}
		}
	}

	int max = 0;
	for(auto it = registers.begin(); it != registers.end(); it++){
		if(it->second > max){
			max = it->second;
		}
	}
	cout << max << " m " << endl;
}
