#include <iostream>
#include <sstream>
#include <algorithm>
using namespace std;

int main(){
	string line;
	int total;
	// for each row
	while(getline(cin, line)){
		istringstream iss(line);	
		int num;
		// for each num
		while(iss >> num){
			// for each num, check for divisible
			istringstream isst(line);
			int val;
			while(isst >> val){
				if(num % val == 0 && num != val){
					// divisible
					total += num / val;
					break;
				}
			}
		}
	}
	cout << total << endl;
	return total;
}
