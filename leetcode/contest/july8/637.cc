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
    vector<double> getAvg;
    vector<double> count;
    vector<double> soln;
public:
    void traverseBST(TreeNode* node, int deep){
        if(node != nullptr){
            // Check if count and getAvg are big enough
            while (deep >= count.size() || deep >= getAvg.size()){
                count.emplace_back(0);
                getAvg.emplace_back(0);
            }
            count[deep] += 1;
            getAvg[deep] += node->val;
            traverseBST(node->left, deep+1);
            traverseBST(node->right, deep+1);
        }
    }
    vector<double> averageOfLevels(TreeNode* root) {
        getAvg.clear();
        cout.clear();
        soln.clear();
        traverseBST(root, 0);
        int leng = count.size();
        for(int i = 0; i < leng; i++){
            cout << getAvg[i] << endl;
            soln.emplace_back(getAvg[i]/count[i]);
        }
        return soln;
    }
};