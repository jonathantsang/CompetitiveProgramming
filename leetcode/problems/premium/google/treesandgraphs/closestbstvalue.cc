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
    double bestdiff = INT_MAX;
    int bestval = INT_MAX;
    void binsearch(TreeNode*node, double target){
        if(node){
            double diff = node->val - target;
            if(diff > 0){
                if(diff < bestdiff){
                    bestdiff = diff;
                    bestval = node->val;
                }
                // go to the left since node->val is larger than target
                binsearch(node->left, target);
            } else if (diff < 0){
                cout << "diff " << abs(diff) << endl;
                if(abs(diff) < bestdiff){
                    cout << "change" << endl;
                    bestdiff = abs(diff);
                    bestval = node->val;
                }
                // go to the right since node->val is less than the target
                binsearch(node->right, target);
            } else {
                // it is 0
                bestdiff = 0;
                bestval = node->val;
                return;
            }
        }
    }
public:
    int closestValue(TreeNode* root, double target) {
        bestdiff = root->val - target;
        if(bestdiff < 0){
            bestdiff = abs(bestdiff);
        }
        bestval = root->val;
        // traverse the tree comparing the number with the values, keep track of the closest number and difference
        binsearch(root, target); // go by bin search    
        return bestval;
    }
};