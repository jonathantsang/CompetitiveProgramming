#include <bits/stdc++.h>
using namespace std;

// 10
// 3 months
// 4, 10 left 6 
// 6, 16 left 10
// 2, 20 left 18
// 18 + 10 = 28

// 10
// 3 months
// 10, 10 left 0
// 2, 10 left 8
// 12, 18 left 6
// 6 + 10 = 16

// 15
// 3 months
// 15, 15 left 0
// 10, 15 left 5
// 20, 20 left 0
// 15

int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int N;
	int months;
	cin >> N >> months; 
	int saved = N;
	int P;
	for(int i = 0; i < months; i++){
		cin >> P;
		saved -= P;
		saved += N;
	}
	cout << saved << endl;
}