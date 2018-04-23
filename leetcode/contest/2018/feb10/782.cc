class Solution {
    bool checkboard(vector<vector<int>> &board){
        int needed = -1;
        for(int i = 0; i < board.size(); i++){
            for(int j = 0; j < board[i].size(); j++){
                if(needed == -1){ // New grid
                    needed = abs(board[0][0] - 1); 
                } else if (needed == -2){ // New row
                    needed = abs(board[i-1][j] -1);
                }
                if(board[i][j] != needed){
                    return false;
                }
            }
            needed = -2; // New row
        }
        return true;
    }
    map<vector<vector<int>>, int> seen;
    bool recurse(vector<vector<int>> board, int moves){
        if(checkboard(board)){
            return moves;
        }
        // Hash
        vector<vector<int>> oldboard = board;
        // Seen
        if(seen.find(board) != seen.end()){
            return 999999;
        }
        else {
            // seen
            seen[board] = 1;
            // Row swap
            for(int i = 0; i < board.size(); i++){
                vector<int> temp = board[i];
                for(int j = 0; j < board.size(); j++){
                    board = oldboard; // Reset
                    temp.clear(); // Store row
                    if(i == j){
                        // Skip same row
                        continue;
                    } else {
                        // Swap the rows, put j in i
                        for(int k = 0; k < board[i].size(); k++){
                            board[i][k] = board[j][k];
                        }
                        // Then put temp in j
                        for(int k = 0; k < board[i].size(); k++){
                            board[j][k] = temp[k];
                        }
                        int b = recurse(board, moves+1);
                        if(b != 999999){
                            return moves;
                        }
                    }
                }
            }
            // Column swap
            // N x N so it is even
            vector<int> temp;
            for(int i = 0; i < board[0].size(); i++){
                // Each column to swap with
                for(int j = 0; j < board[0].size(); j++){
                    board = oldboard;
                    temp.clear();
                    if(i == j){
                        // Skip same row
                        continue;
                    } else {
                        // Store temp
                        for(int k = 0; k < board.size(); k++){
                            temp.push_back(board[k][i]); // Store ith values
                        }
                        // put j in i
                        for(int k = 0; k < board.size(); k++){
                            board[k][i] = board[k][j];
                        }
                        // put temp in j
                        for(int k = 0; k < board.size(); k++){
                            board[k][j] = temp[k];
                        }
                        int b = recurse(board, moves+1);
                        if(b != 999999){
                            return moves;
                        }
                    }
                }
            }
            return 999999; // None worked
        }
    }
public:
    int movesToChessboard(vector<vector<int>>& board) {
        seen.clear();
        int m = recurse(board, 0);
        if(m == 999999){
            return -1;
        } else {
            return m;
        }
    }
};