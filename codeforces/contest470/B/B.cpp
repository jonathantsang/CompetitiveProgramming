#include <bits/stdc++.h>
using namespace std;

void print(vector<int> v){
	for(auto c : v){
		cout << c << " ";
	}
	cout << endl;
}

using namespace std;

bool prime[1000003];
bool v1[1000003];
vector<int> vec;
void sieve(int n)
{
	for(int i = 2; i <= n; i++)
		prime[i] = 1;
	for(int i = 2; i <= n; i++)
	{
		if(prime[i])
		{
			vec.push_back(i);
			for(int j = i; 1LL*j*i <= n; j++)
				prime[i*j] = 0;
		}
	}
}



int main()
{
    // ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	//freopen("input.in", "r", stdin);
	sieve(1000000);
	int n; scanf("%d", &n);
	for(int i : vec)
	{
		if(n%i == 0)
		{
			for(int j = n-i+1; j <= n; j++)
				v1[j] = 1;
		}
	}
	int res = 10000000;
	for(int i : vec)
	{
		for(int j = 2; j*i <= 1000000; j++)
		{
			if(v1[j*i] == 1)
			{
				printf("%d %d\n", j*i, i);
				res = min(j*i-i+1, res);
			}
		}
	}
	printf("%d\n",res);
}