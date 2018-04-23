#include <bits/stdc++.h>
using namespace std;

int main(){
    int x;
    int y;
    int top;
    cin >> x >> y >> top;
    for(int i = 1; i <= top; i++){
    	if(i % x == 0 && i % y == 0){
    		cout << "FizzBuzz" << endl;
    	} else if (i % x == 0){
    		cout << "Fizz" << endl;
    	} else if (i % y == 0){
    		cout << "Buzz" << endl;
    	} else {
    		cout << i << endl;
    	}
    }
}