/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
    // Saves the possible 
    map<int, vector<int>> depths;
public:
    void traverseBST(TreeNode* node, int depth, int pos){
        if(node){
            if(depth == 0){
                depths[depth].emplace_back(pos);
                traverseBST(node->left, depth+1, pos-1);
                traverseBST(node->right, depth+1, pos+1);
            } else {
                depths[depth].emplace_back(pos);
                traverseBST(node->left, depth+1, pos*2);
                traverseBST(node->right, depth+1, pos*2);
            }
        }
    }
    
    int widthOfBinaryTree(TreeNode* root) {
        depths.clear();
        traverseBST(root, 0, 0);
        // Go through map
        int maxDiff = 0;
        for(auto p : depths){
            int leng = p.second.size();
            int max = p.second[0];
            int min = p.second[0];
            // Go through vector looking for max and min number
            for(int i = 0; i < leng; i++){
                if(p.second[i] > max){
                    max = p.second[i];
                }
                if(p.second[i] < min){
                    min = p.second[i];
                }
            }
            // Check if diff is larger than maxDiff
            if(abs(max - min) > maxDiff){
                maxDiff = abs(max-min);
            }
        }
        return maxDiff;
    }
};