#include <bits/stdc++.h>
using namespace std;

int main(){
	float published;
	float impact;
	cin >> published;
	cin >> impact;
	impact--;
	float citations = published * impact;
	citations++;
	cout << citations << endl;
}