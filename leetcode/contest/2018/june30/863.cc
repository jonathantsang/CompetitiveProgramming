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
    vector<int> nodes;
    void dfs(TreeNode *node, TreeNode *target, int dist, int K, int start){
        if(node){
            if(node->val == target->val && dist != K){
                
            }
            if(dist == K){
                if(node->val == target->val){
                    nodes.push_back(start);
                    return;
                } 
                // else skip it
            }
            // mark this node->val is a certain from target
            dfs(node->left, target, dist+1, K, start);
            dfs(node->right, target, dist+1, K, start);
        }
    }
    void allDists(TreeNode *node, TreeNode *target, int K){
        if(node){
            dfs(node, target, 0, K, node->val);
            allDists(node->left, target, K);
            allDists(node->right, target, K);
        }
    }
public:
    vector<int> distanceK(TreeNode* root, TreeNode* target, int K) {
        nodes.clear();
        allDists(root, target, K); // search from root for all of the dists in the tree
        /*
        cout << "path" << endl;
        for(TreeNode*a : path){
            cout << a->val << " ";
        }
        cout << endl;
        */
        // Each of the path work from K-1 to 0 on those nodes
        return nodes;
    }
};