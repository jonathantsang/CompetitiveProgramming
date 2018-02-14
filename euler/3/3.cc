#include <bits/stdc++.h>
using namespace std;

int main(){
	long num = 600851475143;
	for(long i = 2; i < num; i++){
		while(num % i == 0){
			num = num / i;
		}
	}
	cout << num << endl;
}