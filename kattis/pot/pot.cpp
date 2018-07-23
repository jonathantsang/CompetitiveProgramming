#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main(){
	int n;
	cin >> n;
	ll summation = 0;
	while(n--){
		string num;
		cin >> num;
		int exponent = stoi(num.substr(num.length()-1, num.length()));
		int base = stoi(num.substr(0, num.length()-1));
		summation += pow(base, exponent);
	}
	cout << summation << endl;

}