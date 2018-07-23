class Solution {
    bool findWord(vector<vector<char>>& board, int y, int x, int index, string &word, vector<vector<int>> seen){
        // if index == word.length(), we are at the end, meaning the word is found
        if(index == word.length()){
            return true;
        }
        // check in all 9 directions
        // cout << word << " " << y << " " << x << " my index " << index << endl;
        
        // TM
        if(y-1 >= 0 && seen[y-1][x] != 1 && word[index] == board[y-1][x]){
            seen[y][x] = 1;
            index++;
            bool r = findWord(board, y-1, x, index, word, seen);
            if(r){
                return true;
            }
            index--;
            seen[y][x] = 0;
        }
        
        // ML
        if(x-1 < board[0].size()  && seen[y][x-1] != 1 && word[index] == board[y][x-1]){
            seen[y][x] = 1;
            index++;
            bool r = findWord(board, y, x-1, index, word, seen);
            if(r){
                return true;
            }
            index--;
            seen[y][x] = 0;
        }
        
        // MM, not needed since it is where we are currently
        
        // MR
        if(x+1 < board[0].size() && seen[y][x+1] != 1 && word[index] == board[y][x+1]){
            seen[y][x] = 1;
            index++;
            bool r = findWord(board, y, x+1, index, word, seen);
            if(r){
                return true;
            }
            index--;
            seen[y][x] = 0;
        }
        
        // BM
        if(y+1 < board.size() && seen[y+1][x] != 1 && word[index] == board[y+1][x]){
            seen[y][x] = 1;
            index++;
            bool r = findWord(board, y+1, x, index, word, seen);
            if(r){
                return true;
            }
            index--;
            seen[y][x] = 0;
        }

        return false;
    }
    
    bool lookInBoard(vector<vector<char>>& board, string word){
        // Look at each character and if it matches the first one, recurse deeper to try to find the word
        for(int i = 0; i < board.size(); i++){
            for(int j = 0; j < board[i].size(); j++){
                // board[i][j]
                if(board[i][j] == word[0]){
                    // seen has 0 for used, 1 for not used
                    vector<vector<int>> seen;
                    for(int b = 0; b < board.size(); b++){
                        vector<int> row(board[0].size(), 0);
                        seen.push_back(row);
                    }
                    seen[i][j] = 1;
                    bool a = findWord(board, i, j, 1, word, seen);
                    if(a){
                        return true;
                    }
                }
            }
        }
        return false;
    }
public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        vector<string> present;
        map<string, int> seen;
        // for each one of the words
        for(int i = 0; i < words.size(); i++){
            if(seen.count(words[i]) > 0){
                continue;
            }
            // look for it in the board
            bool b = lookInBoard(board, words[i]);
            if(b){
                present.push_back(words[i]);
            }
            seen[words[i]] = 1;
        }
        return present;
    }
};