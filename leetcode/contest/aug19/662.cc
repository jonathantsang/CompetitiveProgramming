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
    map<int, int> counters;
public:
    void traverseBST(TreeNode* node, int depth, bool atLeastOneValidFromParent){
        if(node){
            counters[depth] += 1;
            traverseBST(node->left, depth+1, (node->left || node->right));
            traverseBST(node->right, depth+1, (node->left || node->right));
        } else {
            // Needs to know if the left or right sibling has a valid node, so this can be counted as a valid node
            if(atLeastOneValidFromParent){
                counters[depth] += 1;
            }
        }
    }
    
    int widthOfBinaryTree(TreeNode* root) {
        counters.clear();
        traverseBST(root, 0, (root->left || root->right));
        int maxWidth = 0;
        int maxLevel = 0;
        for(auto p : counters){
            if(p.second > maxWidth){
                maxWidth = p.second;
                maxLevel = p.first;
            }
        }
        return maxWidth;
    }
};