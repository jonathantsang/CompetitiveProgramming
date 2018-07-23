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
    map<TreeNode*, TreeNode*> parents;
    vector<int> nodes;
    map<int, int> seen;
    void dfs(TreeNode *node, TreeNode *parent, int dist, int K){
        if(node){
            parents[node] = parent;
            dfs(node->left, node, dist+1, K);
            dfs(node->right, node, dist+1, K);
        }
    }
    
    void len(TreeNode *node, TreeNode *target, int dist, int K){
        if(node){
            if(seen.count(node->val) > 0){
                return;
            } else {
                seen[node->val] = 1;
            }
            if(dist == K){
                nodes.push_back(node->val);
                return;
            }
            // travel 3 ways
            len(node->left, target, dist+1, K);
            len(node->right, target, dist+1, K);
            len(parents[node], target, dist+1, K);
        }
    }
public:
    vector<int> distanceK(TreeNode* root, TreeNode* target, int K) {
        nodes.clear();
        parents.clear();
        dfs(root, nullptr, 0, K); // make parents
        
        len(target, target, 0, K);
        
        /*
        cout << "path" << endl;
        for(auto k : nodes){
            cout << k << " ";
        }
        cout << endl;
        */
        // Each of the path work from K-1 to 0 on those nodes
        return nodes;
    }
};