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
		
		int first;
		int second;
		iss >> first >> second;

		int max = (first < second ) ?second:first;
		int min = (second < first ) ?second:first;
		int num;
		// for each num
		while(iss >> num){
			if(num > max){
				max = num;
			}
			else if (num < min){
				min = num;
			}
		}
		int rowdiff = max - min;
		total += rowdiff;
	}
	cout << total << endl;
	return total;
}
