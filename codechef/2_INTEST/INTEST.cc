// INTEST
#include <bits/stdc++.h>
using namespace std;

int main(){
	int n;
	int k;
	cin >> n >> k;
	int num = 0;
	int counter = 0;
	int count = 0;
	while(counter < n){
		cin >> num;
		if(num % k == 0){
			count++;
		}
		counter++;
	}
	cout << count << endl;
}