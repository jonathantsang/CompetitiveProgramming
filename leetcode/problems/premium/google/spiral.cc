class Solution {
    vector<int> order;
    vector<vector<int>> seen;
    void traverse(vector<vector<int>> &matrix, int y, int x, string dir){
        if(y < 0 || y >= matrix.size() || x < 0 || x >= matrix[0].size() || seen[y][x] == 1){
            return;
        }
        if(dir == "right"){
            // from matrix[y][x] -> matrix[y][x+...] right until end or seen cell
            while(x >= 0 && x < matrix[0].size() && seen[y][x] == 0){
                seen[y][x] = 1; // mark as seen
                cout << "add " << matrix[y][x] << endl;
                order.push_back(matrix[y][x]);
                x++;
            }
            // exit then go down
            // x-1 since it has to reverse one when it broke the while loop conditions
            traverse(matrix, y+1, x-1, "down");
        }
        else if (dir == "left"){
            // from matrix[y][x] -> matrix[y][x-...] left until end or seen cell
            while(x >= 0 && x < matrix[0].size() && seen[y][x] == 0){
                seen[y][x] = 1; // mark as seen
                cout << "add " << matrix[y][x] << endl;
                order.push_back(matrix[y][x]);
                x--;
            }
            // exit then go up
            // x+1 since it has to reverse one when it broke the while loop conditions
            traverse(matrix, y-1, x+1, "up");
        }
        else if (dir == "up"){
            // from matrix[y][x] -> matrix[y-...][x] up until end or seen cell
            while(y >= 0 && y < matrix.size() && seen[y][x] == 0){
                seen[y][x] = 1; // mark as seen
                cout << "add " << matrix[y][x] << endl;
                order.push_back(matrix[y][x]);
                y--;
            }
            // exit then go down
            // x-1 since it has to reverse one when it broke the while loop conditions
            traverse(matrix, y+1, x+1, "right");
        }
        else if (dir == "down"){
            // from matrix[y][x] -> matrix[y+...][x+...] right until end or seen cell
            while(y >= 0 && y < matrix.size() && seen[y][x] == 0){
                seen[y][x] = 1; // mark as seen
                cout << "add " << matrix[y][x] << endl;
                order.push_back(matrix[y][x]);
                y++;
            }
            // exit then go down
            // x-1 since it has to reverse one when it broke the while loop conditions
            traverse(matrix, y-1, x-1, "left");
        }
    }
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        seen.clear();
        order.clear();
        if(matrix.size() == 0){
            return order;
        }
        seen.resize(matrix.size());
        for(int i = 0; i < seen.size(); i++){
            vector<int> row(matrix[0].size(), 0);
            seen[i] = row;
        }
        // order is right, down, left, up while in seen bounds
        traverse(matrix, 0, 0, "right");
        return order;
    }
};