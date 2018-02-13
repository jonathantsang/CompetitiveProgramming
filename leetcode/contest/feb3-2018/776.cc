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
    TreeNode *parent = nullptr;
public:
    // finds parent of left child where it is less than V
    void FindParent(TreeNode *node, int V){
        // cout << node->val << endl;
        if(!node){
            return;
        }
        // cout << node->val << " dogs"<< endl;
        // cout << node->left->val << " vala" << endl;
        if(node->left && node->left->val <= V){
            // cout << node->val << " cats"<< endl;
            if(parent == nullptr){
                // cout << "set" << endl;
                parent = node;
            }
            return;
        }
        if (node->left) {
            FindParent(node->left, V);
        }
        if (node->right){
            FindParent(node->right, V);
        }
    }
    vector<TreeNode*> splitBST(TreeNode* root, int V) {
        vector<TreeNode*> trees;
        trees.clear();
        if(root == nullptr){
            trees.push_back(nullptr);
            trees.push_back(nullptr);
            return trees;
        } else if(root->val == V){
            trees.push_back(root);
            trees.push_back(nullptr);
            return trees;
        }
        parent = nullptr;
        FindParent(root, V);
        if(parent == nullptr){
            trees.push_back(root);
            trees.push_back(nullptr);
            return trees;
        }
        TreeNode *newtree = parent->left;
        if(newtree->right){
            parent->left = newtree->right;
            newtree->right = nullptr;
        } else if (newtree){
            parent->left = nullptr;
            newtree->right = nullptr;
        }
        trees.push_back(root);
        trees.push_back(newtree);
        return trees;
    }
};