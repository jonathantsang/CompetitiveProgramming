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
    void dfs(TreeNode *node){
        if(node){
            // Leaf
            if(node->left == nullptr && node->right == nullptr){
                order.push_back(node->val);
            } else {
                dfs(node->left);
                dfs(node->right);
            }
        }
    }
public:
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        order.clear();
        dfs(root1);
        vector<int> r1 = order;
        order.clear();
        dfs(root2);
        vector<int> r2 = order;
        if(r1.size() != r2.size()){
            return false;
        }
        for(int i = 0; i < r1.size(); i++){
            if(r1[i] != r2[i]){
                return false;
            }
        }
        return true;
    }
};