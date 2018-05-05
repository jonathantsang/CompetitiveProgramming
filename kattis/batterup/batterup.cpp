#include <bits/stdc++.h>
using namespace std;

int main(){
	int check;
	cin >> check;
	double total;
	double count;
	int num;
	for(int i = 0; i < check; i++){
		cin >> num;
		if(num == -1){
			continue;
		} else {
			total += num;
			count++;
		}
	}
	double avg = total / count;
	cout << fixed;
	cout << setprecision(16) << avg << endl;
}