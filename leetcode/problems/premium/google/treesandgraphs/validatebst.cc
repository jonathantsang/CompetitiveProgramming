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
    vector<int> inorder;
    void traverse(TreeNode *node){
        if(node){
            traverse(node->left);
            inorder.push_back(node->val);
            traverse(node->right);
        }
    }
public:
    bool isValidBST(TreeNode* root) {
        traverse(root);
        // if increasing it is a bst
        for(int i = 1; i < inorder.size(); i++){
            if(!(inorder[i] > inorder[i-1])){
                return false;
            }
        }
        return true;
    }
};