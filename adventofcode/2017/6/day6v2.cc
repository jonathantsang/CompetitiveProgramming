#include <vector>
#include <sstream>
#include <map>
#include <iostream>
using namespace std;

int max(vector<int> &banks){
	int max = 0;
    int index = 0;
	for(int i = 0; i < banks.size(); i++){
		if(banks[i] > max){
			max = banks[i];
			index = i;
		}
   	}
	return index;
}

int run(vector<int> &banks){
	int cycles = 0;
	map<int, int> mem;
	bool go = true;
	// go through banks find max
	while(go){
		int maximal = max(banks);
		cout << maximal << " maximal "<< endl;
		int distribute = banks[maximal];
		banks[maximal] = 0;
		int leng = banks.size();
		int j = maximal + 1;
		j = j % leng;
		while(distribute > 0){
			banks[j] += 1;
			j++;
			j = j % leng;
			distribute--;
		}
		// save current to mem snapshot
        int total = 0;
        for(int i = 0; i < leng; i++){
            total *= 10;
            total += banks[i];
        }
        cycles++;
        cout << total << endl;
        // in the mem
        if(mem.find(total) != mem.end()){
        	// seen once
        	if(mem[total] == 1){
        		mem[total] = cycles;
        	} else {
        		return mem[total] - cycles;
        		exit(1);
        	}
        } else {
        	mem[total] = 1;
        }
        
	}
	return cycles;
}

int main(){
	vector<int> banks;
	int num;
	while(cin >> num){
		banks.emplace_back(num);
	}
	int c = run(banks);
	cout << c << " num" << endl;
}
