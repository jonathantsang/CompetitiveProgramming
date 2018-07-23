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
    int amt;
    int recurseOnNode(TreeNode *node){
        // go to left and right longest path
        if(node){
            int myChain = 0;
            int left = recurseOnNode(node->left);
            int right = recurseOnNode(node->right);
            int leftSide = 0;
            int rightSide = 0;
            if(node->left != nullptr && node->left->val == node->val){
                leftSide = left + 1;
            }
            if(node->right != nullptr && node->right->val == node->val){
                rightSide = right + 1;
            }
            amt = max(amt, leftSide + rightSide);
            return max(leftSide, rightSide);
        }
        return 0;
    }
public:
    int longestUnivaluePath(TreeNode* root) {
        amt = 0;
        recurseOnNode(root);
        return amt;
    }
};