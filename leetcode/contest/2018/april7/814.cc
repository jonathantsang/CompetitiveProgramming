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
    bool recurse(TreeNode *node){
        // want to check if children have a 1
        if(node){
            bool left = recurse(node->left);
            bool right = recurse(node->right);
            // This checks if the branch should be cut since it is not 1 or valid tree
            if(!left){
                node->left = nullptr;
            }
            if(!right){
                node->right = nullptr;
            }
            if(left || right){
                // if left or right is true, have a 1 so it is fine
                return true;
            } else if (node->val == 1){
                // Or if the value is a 1 that is also fine
                return true;
            } else {
                return false;
            }
        } else {
            return false;
        }
        
    }
public:
    TreeNode* pruneTree(TreeNode* root) {
        recurse(root);
        return root;
    }
};