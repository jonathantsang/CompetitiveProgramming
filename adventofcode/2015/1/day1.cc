#include <vector>
#include <sstream>
#include <map>
#include <iostream>
using namespace std;


int main(){
	string input;
	cin >> input;
	int floor = 0;
	for(char c: input){
		if(c == '('){
			floor++;
		}
		else if(c == ')'){
			floor--;
		}
	}
	cout << "f " << floor << endl;
}
