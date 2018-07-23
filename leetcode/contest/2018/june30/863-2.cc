/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
struct LNode {
    int val;
    LNode *left;
    LNode *right;
    LNode *parent;
    
    LNode(int v, LNode*p): val{v}, parent{p}{};
};
class Solution {
    vector<int> nodes;
    LNode *ltarget;
    void dfs(TreeNode *node, LNode *parent, LNode *lnode, TreeNode* target, string dir){
        if(node){
            lnode = new LNode(node->val, parent);
            
            if(node->val == target->val){
                ltarget = lnode;
            }
            if(parent != nullptr && dir == "left"){
                parent->left = lnode;
            } else if (parent != nullptr) {
                parent->right = lnode;
            }
            
            dfs(node->left, lnode, lnode->left, target, "left");
            dfs(node->right, lnode, lnode->right, target, "right");
            cout << node->val << endl;
        }
    }
    void graphTraverse(LNode *node, int dist, int K){
        if(node){
            cout << node->val << endl;
            if(dist == K){
                nodes.push_back(node->val);
                return;
            }
            graphTraverse(node->left, dist+1, K);
            graphTraverse(node->right, dist+1, K);
            graphTraverse(node->parent, dist+1, K);
        }
    }
public:
    vector<int> distanceK(TreeNode* root, TreeNode* target, int K) {
        nodes.clear();
        ltarget = nullptr;
        LNode *linked = nullptr;
        
        dfs(root, nullptr, linked, target, "left"); // search from root for all of the dists in the tree
        
        graphTraverse(ltarget, 0, K);
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