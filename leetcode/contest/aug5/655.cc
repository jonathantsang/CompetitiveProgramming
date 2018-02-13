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
#include <sstream>
public:
    vector<vector<string>> diagram;
    int maxDepth = 0;
    void findDeepest(TreeNode *node, int depth){
        if(node){
            depth++;
            if(depth > maxDepth){
                maxDepth = depth;
            }
            findDeepest(node->left, depth);
            findDeepest(node->right, depth);
        }
    }
    
    void traverseBST(TreeNode *node, int rowLength, int relativeIndex){
        if(node){
            vector<string> row;
            // Prep the row based on rowLength
            // rowLength includes the values in it
            row.resize(rowLength);
            ostringstream oss;
            oss << node->val;
            string value = oss.str();
            row[relativeIndex] = value;
            diagram.emplace_back(row);
            rowLength = rowLength + 2;
            traverseBST(node->left, rowLength, relativeIndex - 1);
            traverseBST(node->right, rowLength, relativeIndex + 1);
        }
    }
    
    vector<vector<string>> printTree(TreeNode* root) {
        diagram.clear();
        maxDepth = 0;
        findDeepest(root, 0);
        cout << maxDepth;
        traverseBST(root, 1, 1);
        return diagram;
    }
};