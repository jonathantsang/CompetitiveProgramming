class Solution {
public:
    bool judgeCircle(string moves) {
        string direction;
        int leng = moves.length();
        int horizontal = 0;
        int vertical = 0;
        for(int i = 0; i < leng; i++){
            if (moves[i] == 'R'){
                horizontal += 1;
            } else if (moves[i] == 'L'){
                horizontal -= 1;
            } else if (moves[i] == 'U'){
                vertical += 1;    
            } else if (moves[i] == 'D'){
                vertical -= 1;
            }
        }
        return ((vertical == 0) && (horizontal == 0));
    }
};