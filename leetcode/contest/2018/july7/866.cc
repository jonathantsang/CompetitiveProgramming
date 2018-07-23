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
    map<TreeNode*, int> depths;
    map<TreeNode *, int> deepestNodes;
    int deepest = 0;
    
    void dfs(TreeNode* node, TreeNode* parent, int depth){
        if(node){
            deepest = max(depth, deepest);
            parents[node] = parent;
            depths[node] = depth;
            
            // nodes[depth].push_back(node);
            
            dfs(node->left, node, depth+1);
            dfs(node->right, node, depth+1);
        }
    }
    
    void findDeepest(TreeNode *node, int depth){
        if(node){
            if(depth == deepest){
                deepestNodes[node] = 1;
            }
            findDeepest(node->left, depth+1);
            findDeepest(node->right, depth+1);
        }
    }
    
    bool checkContains(TreeNode *node, map<TreeNode*, int> &needed){
        if(needed.size() == 2){
            if(needed.count(node->left) > 0 && needed.count(node->right) > 0){
                return true;
            }
        }
        return false;
    }
    
public:
    TreeNode* subtreeWithAllDeepest(TreeNode* root) {
        deepest = 0;
        
        dfs(root, nullptr, 0);
        findDeepest(root, 0);
        
        // Start at the lowest ones and go upwards until parents is size 1
        map<TreeNode *, int> needed;
        for(auto it = deepestNodes.begin(); it != deepestNodes.end(); it++){
            needed[(*it).first] = 1;
        }
        
        while(true){
            if(needed.size() == 1){
                auto beg = needed.begin();
                return (*beg).first;
            } else {
                // size 2 or more, push it up
                TreeNode* beg = (*needed.begin()).first;
                TreeNode* nextOne = (*next(needed.begin())).first;
                
                needed.erase(beg);
                needed.erase(nextOne);
                
                while (depths[beg] > depths[nextOne]){
                    beg = parents[beg];
                }
                while (depths[beg] < depths[nextOne]){
                    nextOne = parents[nextOne];
                }
                // same depth now, work up until at the same node
                while(beg != nextOne){
                    beg = parents[beg];
                    nextOne = parents[nextOne];
                }
                // same node now
                needed[beg] = 1;
                
                if(needed.size() == 1){
                    return beg;
                }
            } 
            /*
            for(map<TreeNode*, int>::iterator it = needed.begin(); it != needed.end(); it++){
                // get the parent of each needed and add to needed
                TreeNode * node = (*it).first;
                needed.erase((*it).first);
                needed[parents[node]] = 1; // add the parent
            }
            */
        }
        
        return root;
    }
};