#include <iostream>
#include <vector>
#include <sstream>
#include <string>

using namespace std;
int main(){
	string input;
	cin >> input;
	string str = input;
	int total = 0;
	for(int i = 0; i < str.length(); i++){
		if(i == 0){
			if(str[0] == str[str.length()-1]){
            	int value = str[i] - '0';
            	total += value;
        	}
		}
		else if(str[i] == str[i-1]){
			int value = str[i] - '0';
			total += value;
		}
	}
	cout << total << endl;
	return total;
}
