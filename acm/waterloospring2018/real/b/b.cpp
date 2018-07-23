#include <bits/stdc++.h>
using namespace std;

vector<long> primes;

void setup(){
	primes.clear();
	primes.push_back(2);
	primes.push_back(3);
	primes.push_back(5);
	primes.push_back(7);
	primes.push_back(11);
	// unsigned long long a = 2000000000;
	long a = 25000000;
	for(long i = 13; i < a; i+=2){
		if(i % 2 == 0 || i % 3 == 0 || i % 5 == 0 || i % 7 == 0 || i % 11 == 0 || i % 13 == 0){
			continue;
		}
		primes.push_back(i);
	}
}

bool checkprime(long num){
	long mid = sqrt(num);
	/*
	if(num % 2 == 0) return false;
	for(int i = 3; i <= mid; i+=2){
		if(num % i == 0){
			return false;
		}
	}
	*/
	for(long i = 0; i < primes.size(); i++){
		// cout << "at " << primes[i] << " " << num << endl;
		if(num % primes[i] == 0){
			return false;
		}
		if(primes[i] > mid || primes[i] > num){
			return true;
		}
	}
	return true;
}

long findnextprime(long num){
	// onwards num
	bool notprime = true;
	if(num % 2 == 0) num++;
	while(notprime){
		if(checkprime(num)){
			return num;
		}
		num+=2;
	}
	return num;
}

int main(){
	setup();
	long amt;
	cin >> amt;
	for(long i = 0; i < amt; i++){
		long num;
		cin >> num;
		if(num == 0 || num == 1){
			cout << 2 << endl;
			continue;
		}
		long nextprime = findnextprime(num);
		cout << nextprime << endl;
	}
}