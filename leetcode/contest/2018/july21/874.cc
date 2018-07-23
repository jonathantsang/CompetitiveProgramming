class Solution {
    map<pair<int,int>, int> objects;
    int x;
    int y;
    
    int rotate(int direction, int dir){
        if(direction == 0){
            if(dir == -1){
                direction = 1;
            } else if (dir == -2){
                direction = 3;
            }
        }
        else if (direction == 1){
            if(dir == -1){
                direction = 2;
            } else if (dir == -2){
                direction = 0;
            }
        }
        else if (direction == 2){
            if(dir == -1){
                direction = 3;
            } else if (dir == -2){
                direction = 1;
            }
        }
        else if (direction == 3){
            if(dir == -1){
                direction = 0;
            } else if (dir == -2){
                direction = 2;
            }
        }
        return direction;
    }
    
    void move(int direction, int amount){
        // move from x, y to some other space, and check for anything in the way
        for(int i = 0; i < amount; i++){
            // cout << x << " " << y << endl;
            if(direction == 0){
                if(objects.count(make_pair(x, y+1))){
                    //cout << "hit" << endl;
                    return; // Stop movement due to obstacle
                } else {
                    y++;
                }
            }
            else if (direction == 1){
                if(objects.count(make_pair(x+1, y))){
                    // cout << "hit" << endl;
                    return; // Stop movement due to obstacle
                } else {
                    x++;
                }
            }
            else if (direction == 2){
                if(objects.count(make_pair(x, y-1))){
                    // cout << "hit" << endl;
                    return; // Stop movement due to obstacle
                } else {
                    y--;
                }
            }
            else if (direction == 3){
                if(objects.count(make_pair(x-1, y))){
                    // cout << "hit" << endl;
                    return; // Stop movement due to obstacle
                } else {
                    x--;
                }
            }
        }
    }
public:
    int robotSim(vector<int>& commands, vector<vector<int>>& obstacles) {
        objects.clear();
        int direction = 0; // 0 north, 1 right, 2 down, 3 left
        x = 0;
        y = 0;
        
        // make obstacles
        for(int i = 0; i < obstacles.size(); i++){
            // cout << "add " << obstacles[i][0] << " " << obstacles[i][1] << endl;
            objects[make_pair(obstacles[i][0], obstacles[i][1])] = 1;
        }
        
        for(int i = 0; i < commands.size(); i++){
            // turn
            if(commands[i] < 0){
                if(commands[i] == -1){
                    // turn right 90 degrees
                    direction = rotate(direction, -1);
                    // direction = (direction + 1) % 4;
                } else if (commands[i] == -2) {
                    // turn left 90 degrees
                    direction = rotate(direction, -2);
                    // direction = (direction - 1);
                    // direction = direction == -1 ? 3 : direction; // case where it is negative
                }
            } else {
                // movement
                 move(direction, commands[i]);
            }
            // cout << x << " " << y << endl;
        }
        cout << x << " " << y << endl;
        // Get x and y
        int a = pow(x, 2);
        int b = pow(y, 2);
        return a + b;
    }
};