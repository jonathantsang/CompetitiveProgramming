#include <vector>
#include <sstream>
#include <map>
#include <iostream>
using namespace std;


int main(){
	string input;
	cin >> input;
	int floor = 0;
	int i = 0;
	for(char c: input){
		i++;
		if(c == '('){
			floor++;
		}
		else if(c == ')'){
			floor--;
			if(floor < 0){
				cout << "s " << i << endl;
				exit(1);
			}
		}

	}
	cout << "f " << floor << endl;
}
