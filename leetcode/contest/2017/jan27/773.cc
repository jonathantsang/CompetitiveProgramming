class Solution {
    map<int, int> solved;
    int recurse(vector<vector<int>> board, int steps){
        // Check if solved, hash to six digit num
        int val = board[0][0] * 100000 + board[0][1] * 10000 + board[0][2] * 1000 + board[1][0] * 100 + board[1][1] * 10 + board[1][2];
        // cout << val << endl;
        // Check if the solved is the correct hash
        if(val == 123459){
            // cout << steps << endl;
            return steps;
        }
        // new value
        if(solved.find(val) == solved.end()){
            solved[val] = steps;
        } else {
            // old value, but check, this is tricky
            if(solved[val] > steps){
                solved[val] = steps;
                // attempt to find solution with shorter steps
            } else {
                // took too long by comparison
                return 999;
            }
            
            
        }
        // Go further checking the swaps the 0 (9) can do
        int i = 0;
        int j = 0;
        bool exit = false;
        for(i = 0; i < board.size(); i++){
            for(j = 0; j < board[i].size(); j++){
                if(board[i][j] == 9){
                    exit = true;
                    break;
                }
            }
            if(exit == true){
                break;
            }
        }
        // Find coordinates of the 0 (9) for swaps
        // If it j = 1, it is in a middle row with 3 possibilities
        int temp = 0;
        if(j == 1){
            if(i == 0){
                // Top row
                // Left
                vector<vector<int>> board1 = board;
                temp = board1[0][0];
                board1[0][0] = board1[0][1];
                board1[0][1] = temp;
                // Right
                vector<vector<int>> board2 = board;
                temp = board2[0][2];
                board2[0][2] = board2[0][1];
                board2[0][1] = temp;
                // Middle
                vector<vector<int>> board3 = board;
                temp = board3[1][1];
                board3[1][1] = board3[0][1];
                board3[0][1] = temp;
                int steps1 = recurse(board1, steps+1);
                int steps2 = recurse(board2, steps+1);
                int steps3 = recurse(board3, steps+1);
                return min(min(steps1, steps2), steps3);
            } else {
                // Left
                vector<vector<int>> board1 = board;
                temp = board1[1][0];
                board1[1][0] = board1[1][1];
                board1[1][1] = temp;
                // Right
                vector<vector<int>> board2 = board;
                temp = board2[1][2];
                board2[1][2] = board2[1][1];
                board2[1][1] = temp;
                // Middle
                vector<vector<int>> board3 = board;
                temp = board3[0][1];
                board3[0][1] = board3[1][1];
                board3[1][1] = temp;
                int steps1 = recurse(board1, steps+1);
                int steps2 = recurse(board2, steps+1);
                int steps3 = recurse(board3, steps+1);
                return min(min(steps1, steps2), steps3);
            }
        } else {
            // Else it is on the edge
            if(i == 0 && j == 0){
                vector<vector<int>> board1 = board;
                vector<vector<int>> board2 = board;
                // Right
                temp = board1[0][1];
                board1[0][1] = board1[0][0];
                board1[0][0] = temp;
                // Down
                temp = board2[1][0];
                board2[1][0] = board2[0][0];
                board2[0][0] = temp;
                int steps1 = recurse(board1, steps+1);
                int steps2 = recurse(board2, steps+1);
                return min(steps1, steps2);
            } else if (i == 0 && j == 2){
                vector<vector<int>> board1 = board;
                vector<vector<int>> board2 = board;
                // Left
                temp = board1[0][1];
                board1[0][1] = board1[0][2];
                board1[0][2] = temp;
                // Down
                temp = board2[1][2];
                board2[1][2] = board2[0][2];
                board2[0][2] = temp;
                int steps1 = recurse(board1, steps+1);
                int steps2 = recurse(board2, steps+1);
                return min(steps1, steps2);
            } else if (i == 1 && j == 0){
                vector<vector<int>> board1 = board;
                vector<vector<int>> board2 = board;
                // Up
                temp = board1[0][0];
                board1[0][0] = board1[1][0];
                board1[1][0] = temp;
                // Right
                temp = board2[1][1];
                board2[1][1] = board2[1][0];
                board2[1][0] = temp;
                int steps1 = recurse(board1, steps+1);
                int steps2 = recurse(board2, steps+1);
                return min(steps1, steps2);
            } else if (i == 1 && j == 2){
                vector<vector<int>> board1 = board;
                vector<vector<int>> board2 = board;
                // Up
                temp = board1[0][2];
                board1[0][2] = board1[1][2];
                board1[1][2] = temp;
                // Left
                temp = board2[1][1];
                board2[1][1] = board2[1][2];
                board2[1][2] = temp;
                int steps1 = recurse(board1, steps+1);
                int steps2 = recurse(board2, steps+1);
                return min(steps1, steps2);
            }
        }
        return 999;
    }
public:
    int slidingPuzzle(vector<vector<int>>& board) {
        solved.clear();
        // Set 0 to 9, so front of val is not messed up
        for(int i = 0; i < board.size(); i++){
            for(int j = 0; j < board[i].size(); j++){
                if(board[i][j] == 0){
                    board[i][j] = 9;
                }
            }
        }
        int moves = recurse(board, 0);
        if(moves == 999){
            return -1;
        }
        return moves;
    }
};