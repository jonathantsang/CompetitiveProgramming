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
    vector<TreeNode *> inorder;
    void traverse(TreeNode *node){
        if(node){
            traverse(node->left);
            inorder.push_back(node);
            traverse(node->right);
        }
    }
public:
    TreeNode* inorderSuccessor(TreeNode* root, TreeNode* p) {
        inorder.clear();
        traverse(root);
        for(int i = 0; i < inorder.size(); i++){
            if(inorder[i]->val == p->val){
                if(i+1 == inorder.size()){
                    return nullptr;
                } else {
                    return inorder[i+1];
                }
            }
        }
        return nullptr;
    }
};