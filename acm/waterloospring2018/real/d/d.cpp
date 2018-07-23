#include <bits/stdc++.h>
using namespace std;

bool checkwin(vector<vector<char>>& board){
	int X = 0;
	int O = 0;
	// rows
	for(int i = 0; i < board.size(); i++){
		char comp = board[i][0];
		if(comp == 'E'){
			continue;
		}
		bool all = true;
		for(int j = 0; j < board.size(); j++){
			if(board[i][j] != comp){
				all = false;
				break;
			}
		}
		if(all == true){
			if(comp == 'X'){
				X++;
			} else {
				O++;
			}
		}
	}
	// columns
	for(int i = 0; i < board.size(); i++){
		char comp = board[0][i]; // of column i
		if(comp == 'E'){
			continue;
		}
		bool all = true;
		for(int j = 0; j < board.size(); j++){
			// board[j][i]
			if(board[j][i] != comp){
				all = false;
				break;
			}
		}
		if(all == true){
			if(comp == 'X'){
				X++;
			} else {
				O++;
			}
		}
	}
	if(X > O){
		cout << "X WINS" << endl;
		return true;
	} else if (O > X) {
		cout << "O WINS" << endl;
		return true;
	}
	return false;
}

void makeMove(char dir, char num, vector<vector<char>>& board, char turn){
	int x = -1;
	int y = -1;
	// Alter at board[y][x] based on turn and direction
	if(dir == 'L'){
		x = 0;
		y = num-1;

		if(board[y][x] == 'E'){
			board[y][x] = turn;
			return;
		}

		// furthest NOT E
		int furthest = board.size()-1;

		for(int i = 0; i < board.size(); i++){
			if(board[y][i] == 'E'){
				furthest = i;
				break;
			}
		}
		// push over to the left
		for(int i = furthest; i > 0; i--){
			board[y][i] = board[y][i-1];
		}
		board[y][x] = turn;
		
	} else if (dir == 'R'){
		x = board.size()-1;
		y = num-1;

		if(board[y][x] == 'E'){
			board[y][x] = turn;
			return;
		}

		// furthest NOT E
		int furthest = 0;

		for(int i = board.size()-1; i >= 0; i--){
			if(board[y][i] == 'E'){
				furthest = i;
				break;
			}
		}
		
		// push over to the left
		for(int i = furthest; i < board.size()-1; i++){
			board[y][i] = board[y][i+1];
		}
		board[y][x] = turn;
		
	} else if (dir == 'T'){
		y = 0;
		x = num-1;

		if(board[y][x] == 'E'){
			board[y][x] = turn;
			return;
		}

		int furthest = board.size()-1;

		// find furthest downwards that is E
		for(int i = 0; i < board.size(); i++){
			if(board[i][x] == 'E'){
				furthest = i;
				break;
			}
		}

		// have to shift downwards
		for(int i = furthest; i > 0; i--){
			board[i][x] = board[i-1][x];
		}

		board[y][x] = turn;
	} else if (dir == 'B'){
		y = board.size()-1;
		x = num-1;

		if(board[y][x] == 'E'){
			board[y][x] = turn;
			return;
		}

		int furthest = 0;

		// find furthest upwards that is E
		for(int i = board.size()-1; i >= 0; i--){
			if(board[i][x] == 'E'){
				furthest = i;
				break;
			}
		}

		// have to shift upwards
		for(int i = furthest; i < board.size()-1; i++){
			board[i][x] = board[i+1][x];
		}
		board[y][x] = turn;
	}
}

void print(vector<vector<char>>& board){
	for(auto row : board){
		for(char c : row){
			cout << c << " ";
		}
		cout << endl;
	}
	cout << endl;
}

int main(){
	int N;
	cin >> N;
	vector<vector<char>> board(N, vector<char>(N, 'E'));
	string move;
	// print(board);
	char turn = 'X';
	getline(cin, move);
	while(getline(cin, move)){
		if(move == "QUIT"){
			cout << "TIE GAME" << endl;
			break;
		}
		char dir;
		int num;
		istringstream iss{move};
		iss >> dir >> num;
		// make the move
		makeMove(dir, num, board, turn);
		// print(board);
		turn = turn == 'X' ? 'O' : 'X';
		if(checkwin(board)){
			break;
		}
	}
}