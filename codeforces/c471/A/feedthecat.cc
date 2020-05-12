#include <bits/stdc++.h>
using namespace std;

int minsto20(int h, int m){
	int twentyo = 20 * 60; // minutes
	int reg = h * 60 + m;
	if(reg > twentyo){
		return 0;
	} else {
		return twentyo - reg;
	}
}

int main(){
	string line;
	getline(cin, line);
	istringstream isst{line};
	int hour;
	int min;
	isst >> hour >> min;

	// Get HDCN
	getline(cin, line);
	istringstream iss{line};
	int H;
	int D;
	int C;
	int N;
	iss >> H >> D >> C >> N;

	// Calculate immediate feeding
	int amt_needed = H / N;
	// Round up if necessary
	if(H % N != 0){
		amt_needed++;
	}
	float immediate_cost = amt_needed * C;

	// Going to 20:00 discount time
	int diff = minsto20(hour, min); // number of mins until discount
	int cat_hunger_later = H + D * diff;
	int new_amt_needed = cat_hunger_later / N;
	// Round up if necessary
	if(cat_hunger_later % N != 0){
		new_amt_needed++;
	}
	float later_cost = new_amt_needed * (C * 0.8);

	float final = std::min(immediate_cost, later_cost);
	std::cout << std::fixed;
    std::cout << std::setprecision(4);
	cout << final << endl;

}