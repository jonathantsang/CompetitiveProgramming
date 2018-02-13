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
	int leng = str.length();
	int jump = leng / 2;
	for(int i = 0; i < str.length(); i++){
		int newplace = (i + jump) % leng;
		if(str[i] == str[newplace]){
			int value = str[i] - '0';
			total += value;
		}
	}
	cout << total << endl;
	return total;
}
