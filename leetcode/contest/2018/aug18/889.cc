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
public:
    TreeNode* constructFromPrePost(vector<int>& pre, vector<int>& post) {
        TreeNode * start = new TreeNode(pre[0]);
        if(pre.size() == 1){
            return start;
        }
        int preIdx = 1;
        int postIdx = 0;
        TreeNode *cur = start;
        
        map<TreeNode*, TreeNode*> parent;
        parent[start] = nullptr;
        set<int> preSeen;
        
        while(preIdx < pre.size() && postIdx < post.size()){
            if(cur->val == post[postIdx]){
                // Find the parent
                // cout << cur->val << " parent is " << parent[cur]->val << endl;
                cur = parent[cur]; // move up one level
                postIdx++;
                while(preSeen.count(post[postIdx]) != 0){
                    // cout << "already seen " << post[postIdx] << endl;
                    cur = parent[cur];
                    postIdx++; // already seen
                }
                
            } else {
                // Keep branching left or if taken right
                if(cur->left != nullptr){
                    TreeNode *right = new TreeNode(pre[preIdx]);
                    // cout << "add " << pre[preIdx] << " child of " << cur->val << endl;
                    parent[right] = cur;
                    cur->right = right;
                    cur = right;
                    
                    preSeen.insert(pre[preIdx]);
                    preIdx++;
                } else {
                    TreeNode *left = new TreeNode(pre[preIdx]);
                    // cout << "add " << pre[preIdx] << " child of " << cur->val << endl;
                    parent[left] = cur;
                    cur->left = left;
                    cur = left;
                    
                    preSeen.insert(pre[preIdx]);
                    preIdx++;
                }
            }
        }
        return start;
    }
};