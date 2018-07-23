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
    int bestLeft = 0;
    vector<int> leftPath;
    vector<int> leaves;
    int bestRight = 0;
    vector<int> rightPath;
    vector<int> entire;
    map<int, int> seen;
    void checkLeft(TreeNode* node, vector<int> nodes, int left){
        if(node){
            nodes.push_back(node->val);
            checkLeft(node->left, nodes, left+1);
            checkLeft(node->right, nodes, left-1);
        }
        // Not a valid one check
        if(left > bestLeft){
            leftPath = nodes;
            bestLeft = left;
        }
    }
    void checkLeaves(TreeNode *node){
        if(node){
            // leaf
            if(node->left == nullptr && node->right == nullptr){
                leaves.push_back(node->val);
            } else {
                checkLeaves(node->left);
                checkLeaves(node->right);
            }
        }
    }
    void checkRight(TreeNode* node, vector<int> nodes, int right){
        if(node){
            nodes.push_back(node->val);
            checkRight(node->left, nodes, right-1);
            checkRight(node->right, nodes, right+1);
        }
        // Not a valid one check
        if(right > bestRight){
            rightPath = nodes;
            bestRight = right;
        }
    }
public:
    vector<int> boundaryOfBinaryTree(TreeNode* root) {
        leftPath.clear();
        leaves.clear();
        rightPath.clear();
        entire.clear();
        if(root == nullptr){
            return entire;
        }
        
        if(root->left == nullptr && root->right == nullptr){
            entire.push_back(root->val);
            return entire;
        }
        if(root->left == nullptr){
            leftPath.push_back(root->val);
        }
        if(root->right == nullptr){
            rightPath.push_back(root->val);
        }
        
        vector<int> arr;
        if(leftPath.empty()){
            arr.push_back(root->val);
            checkLeft(root, arr, 1);
        }
        
        // update seen
        for(int v : leftPath){
            seen[v] = 1;
        }
        
        checkLeaves(root);
        
        // update seen, remove leaves that are in the left path
        vector<int> remDuplicates;
        for(int v : leaves){
            if(seen.count(v) == 0){
                remDuplicates.push_back(v);
            }
        }
        leaves = remDuplicates;
        for(int v : leaves){
            seen[v] = 1;
        }
            
        vector<int> arr2;
        if(rightPath.empty()){
            checkRight(root->right, arr2, 1);
        }
        
        // update seen, remove leaves that are in the left path and leaves
        vector<int> newone;
        for(int v : rightPath){
            if(seen.count(v) == 0){
                newone.push_back(v);
            }
        }
        rightPath = newone;
        for(int v : rightPath){
            seen[v] = 1;
        }
        
        // right will be swapped to what we want
        reverse(rightPath.begin(), rightPath.end());
        
        cout << "left" << endl;
        for(int a : leftPath){
            entire.push_back(a);
            cout << a << endl;
        }
        //cout << "leaves" << endl;
        for(int b : leaves){
            entire.push_back(b);
            //cout << b << endl;
        }
        //cout << "right" << endl;
        for(int c : rightPath){
            entire.push_back(c);
            //cout << c << endl;
        }
        return entire;
    }
};
