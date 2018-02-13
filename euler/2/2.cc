#include <bits/stdc++.h>
using namespace std;

int main(){
	unsigned long long int last2 = 1;
	unsigned long long int last1 = 2;
	unsigned long long int i = 3;
	unsigned long long int sum = 2; // Start with 2
	unsigned long long int limit = 4000000;
	while(i <= limit){
		if(i % 2 == 0){
			sum += i;
		}
		i = last1 + last2;
		last2 = last1;
		last1 = i;
		// cout << i << endl;
	}
	cout << sum << endl;
}