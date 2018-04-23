/*
a = abs(x * sin(o)) + abs(y * cos(o))
b = abs(x * cos(o)) + abs(y * sin(o))
*/

#include <bits/stdc++.h>
using namespace std;

int main(){
	int cases;
	string line;
	cin >> cases;
	getline(cin, line);
	for(int c = 0; c < cases; c++){
		getline(cin, line);
		istringstream iss{line};
		int areaWanted;
		iss >> areaWanted;

		vector<float> face1 {0.5, 0, 0};
		vector<float> face2 {0, 0.5, 0};
		vector<float> face3 {0, 0, 0.5};

		pair<float, float> tr {1, 1}; // 2D
		pair<float, float> bl {0, 0}; // 2D
		pair<float, float> tl {0, 1}; // 2D
		pair<float, float> br {1, 0}; // 2D
		float center = 0.5;

		// Keep rotating tr until it reaches
		tr.first = (tr.first - center) * cos(45) - (tr.first - center) * sin(45);
		tr.second = (tr.second - center) * cos(45) + (tr.second - center) * sin(45);

		// translate back
		tr.first += center;
		tr.second += center;

		cout << tr.first << " " << tr.second << endl;

		// Keep rotating bl until it reaches
		bl.first = (bl.first - center) * cos(45) - (bl.first - center) * sin(45);
		bl.second = (bl.second - center) * cos(45) + (bl.second - center) * sin(45);

		// translate back
		bl.first += center;
		bl.second += center;

		cout << bl.first << " " << bl.second << endl;

		// Keep rotating bl until it reaches
		tl.first = (tl.first - center) * cos(45) - (tl.first - center) * sin(45);
		tl.second = (tl.second - center) * cos(45) + (tl.second - center) * sin(45);

		// translate back
		tl.first += center;
		tl.second += center;

		cout << tl.first << " " << tl.second << endl;

		// Keep rotating bl until it reaches
		br.first = (br.first - center) * cos(45) - (br.first - center) * sin(45);
		br.second = (br.second - center) * cos(45) + (br.second - center) * sin(45);

		// translate back
		br.first += center;
		br.second += center;

		cout << br.first << " " << br.second << endl;

		// X value
		float maximum = max(br.first, max(bl.first, max(tl.first, tr.first)));
		float minimum = min(br.first, min(bl.first, min(tl.first, tr.first)));

		// If this gives the desired areas
		cout << maximum << " " << minimum << endl;
		cout << "width is " << maximum - minimum << endl;

		// rotate the face1 and face2 by that angle

		cout << "Case #" << c+1 << ": " << endl;
	}
}