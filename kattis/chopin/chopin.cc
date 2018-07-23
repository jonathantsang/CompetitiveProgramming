#include <bits/stdc++.h>
using namespace std;

int main(){
	string line;
	int i = 1;
	while(getline(cin, line)){
		istringstream iss{line};
		string note;
		string tonality;
		iss >> note >> tonality;
		if(note == "A#"){
			note = "Bb";
		} else if (note == "Bb"){
			note = "A#";
		} else if (note == "C#"){
			note = "Db";
		} else if (note == "Db"){
			note = "C#";
		} else if (note == "D#"){
			note = "Eb";
		} else if (note == "Eb"){
			note = "D#";
		} else if (note == "F#"){
			note = "Gb";
		} else if (note == "Gb"){
			note = "F#";
		} else if (note == "G#"){
			note = "Ab";
		} else if (note == "Ab"){
			note = "G#";
		} else {
			cout << "Case " << i << ": " << "UNIQUE" << endl;
			continue;
			i++;
		}

		cout << "Case " << i << ": " << note << " " << tonality << endl;
		i++;
	}
}