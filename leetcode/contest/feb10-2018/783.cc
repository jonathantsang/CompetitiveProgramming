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
    vector<int> vals;
    void recurse(TreeNode *node){
        if(node){
            vals.push_back(node->val);
            recurse(node->left);
            recurse(node->right);
        }
    }
public:
    int minDiffInBST(TreeNode* root) {
        vals.clear();
        recurse(root);
        sort(vals.begin(), vals.end());
        int diff = abs(vals[0] - vals[1]);
        for(int i = 1; i < vals.size(); i++){
            int d = vals[i] - vals[i-1];
            if(d < diff){
                diff = d;
            }
        }
        return diff;
    }
};