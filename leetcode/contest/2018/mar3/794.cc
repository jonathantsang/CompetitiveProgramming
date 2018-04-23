class Solution {
public:
    bool validTicTacToe(vector<string>& board) {
        int x = 0;
        int o = 0;
        int winx = 0;
        int wino = 0;
        for(int i = 0; i < board.size(); i++){
            bool all = board[i][0] == board[i][1] && board[i][1] == board[i][2] ? true : false;
            char first = board[i][0];
            for(int j = 0; j < 3; j++){
                if(board[i][j] == 'X'){
                    x++;
                } else if (board[i][j] == 'O'){
                    o++;
                }
            }
            if(all && board[i][0] != ' '){
                if(first == 'X' && winx == 1){
                    return false;
                }
                if(first == 'X'){
                    winx++;
                }
                if(first == 'O' && wino == 1){
                    return false;
                }
                if(first == 'O'){
                    wino++;
                }
            }
        }
        for(int i = 0; i < board.size(); i++){
            bool all = board[0][i] == board[1][i] && board[1][i] == board[2][i] ? true : false;
            char first = board[0][i];
            if(all && board[0][i] != ' '){
                if(first == 'X' && winx == 1){
                    return false;
                }
                if(first == 'X')
                    winx++;
                if(first == 'O' && wino == 1){
                    return false;
                }
                if(first == 'O'){
                    wino++;
                }
            }
        }
        
        char first = board[1][1];
        if(board[0][0] == board[1][1] && board[1][1] == board[2][2]){
            if(first == 'X' && winx == 1){
                return false;
            }
            if(first == 'X'){
                winx++;
            }
            if(first == 'O' && wino == 1){
                return false;
            }
            if(first == 'O'){
                wino++;
            }
        }
        // Diag
        if(board[0][2] == board[1][1] && board[2][0] == board[1][1]){
            if(first == 'X' && winx == 1){
                return false;
            }
            if(first == 'X'){
                winx++;
            }
            if(first == 'O' && wino == 1){
                return false;
            }
            if(first == 'O'){
                wino++;
            }
        }
        
        if(winx == 1){
            return x == o + 1;
        } 
        if(wino == 1){
            return x == o;
        }
        if(o == x){
            return true;
        }
        if(o > x){
            return false;
        }
        if(abs(x - o) >= 2){
            return false;
        }
        return true;
    }
};