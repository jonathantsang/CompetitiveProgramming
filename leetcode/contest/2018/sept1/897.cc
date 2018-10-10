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
    vector<int> order;
    void recurse(TreeNode* node){
        if(node){
            recurse(node->left);
            order.push_back(node->val);
            recurse(node->right);
        }
    }
public:
    TreeNode* increasingBST(TreeNode* root) {
        recurse(root);
        // Construct from order
        TreeNode *start = new TreeNode(order[0]);
        TreeNode *node = start;
        for(int i = 1; i < order.size(); i++){
            node->right = new TreeNode(order[i]);
            node = node->right;
        }
        return start;
    }
};