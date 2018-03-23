#include <bits/stdc++.h>
using namespace std;

int main(){
    string word;
    while(cin >> word){
        int counter = 0;
            for(int i = 0; i < word.length(); i++){
                if(word[i] == 'B'){
                    counter++;
                } else {
                    counter--;
                }
            }
        int result = counter == 0 ? 1 : 0;
        cout << result << endl;
    }
}