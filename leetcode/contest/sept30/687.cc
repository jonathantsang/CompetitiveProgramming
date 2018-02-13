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
    map<int, int> lastSeen;
    map<int, int> leftSide;
    int distMax;
    void recurseTree(TreeNode* node){
        
        // Every time further, decrement all lastSeen by 1
        for(std::map<int,int>::iterator iter = lastSeen.begin(); iter != lastSeen.end(); ++iter){
            lastSeen[iter->first] -= 1;
        }
        
        // If the node is not in the map, add it
        if(lastSeen.find(node->val) == lastSeen.end()){
            lastSeen[node->val] = 0;
        } else {
            // Else it is in there, so see when it was seen last
            int previouslySeen = -lastSeen[node->val];
            if(previouslySeen > distMax){
                distMax = previouslySeen;
            }
        }
        
        if(node->left){
            leftSide[node->left->val];
            recurseTree(node->left);
        }
        
        // Increment top due to going up
        map<int,int> doneAlready;
        for(std::map<int,int>::iterator iter = lastSeen.begin(); iter != lastSeen.end(); ++iter){
            // Not in the leftSide, increment by 1
            if(doneAlready.find(iter->first) == lastSeen.end() && leftSide.find(iter->first) == lastSeen.end()){
                lastSeen[iter->first] += 1;
                doneAlready[iter->first] = 1;
            }
        }
        
        if(node->right){
            leftSide[node->right->val];
            recurseTree(node->right);
        }
    
    }
    
public:
    int longestUnivaluePath(TreeNode* root) {
        lastSeen.clear();
        distMax = 0;
        leftSide.clear();
        recurseTree(root);
        return distMax;
    }
};