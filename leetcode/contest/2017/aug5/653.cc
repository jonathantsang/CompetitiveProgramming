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
vector<int> nodes;
public:
    void traverseBST(TreeNode *node){
        nodes.emplace_back(node->val);
        if(node->left){
            traverseBST(node->left);
        }
        if(node->right){
            traverseBST(node->right);
        }
    }
    
    bool findTarget(TreeNode* root, int k) {
        nodes.clear();
        traverseBST(root);
        int leng = nodes.size();
        for(int i = 0; i < leng; i++){
            for(int j = 0; j < leng; j++){
                if(i != j){
                    if(nodes[i] + nodes[j] == k){
                        return true;
                    }
                }
            }
        }
        return false;
    }
};