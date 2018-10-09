#include <bits/stdc++.h>
using namespace std;

bool isPrime(int n){
	if(n == 2){
		return true;
	}
	if(n % 2 == 0){
		return false;
	}
	for(int i = 3; i < sqrt(n)+1; i+=2){
		if((n % i) == 0){
			return false;
		}
	}
	return true;
}

int main() {
	int val;
	while(cin >> val){

		if(val == 0){
			break;
		}

		int twoTimes = val * 2 + 1;


		while(!isPrime(twoTimes)){
			twoTimes++;
		}

		cout << twoTimes;

		if(!isPrime(val)){
			cout << " (" << val << " is not prime)" << endl;
		} else {
			cout << endl;
		}

	}
}