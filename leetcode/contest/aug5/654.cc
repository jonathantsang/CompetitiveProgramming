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
    // End needs to be equal to the end since i <= end
    // This will return the INDEX of the maximum value
    int findMaxIndex(vector<int>& nums, int start, int end){
        int max = -1;
        int maxIndex = -1;
        for(int i = start; i <= end; i++){
            if(nums[i] > max){
                maxIndex = i;
                max = nums[i];
            }
        }
        return maxIndex;
    }
    void constructNodes(TreeNode *node, vector<int>&nums, int start, int end, string direction){
        // Needs to be strictly less, or no more nodes to construct
        if(start <= end){
            
            // Case if start == end
            if(start == end){
                int maximum = start;
                TreeNode *newNode = new TreeNode(nums[maximum]);
                if(direction == "right"){
                    node->right = newNode;
                } else if (direction == "left"){
                    node->left = newNode;
                }
                // End it here since it is only one node in the space
                return;
            }
            
            int maximum = findMaxIndex(nums, start, end);
            if(maximum < 0){
                return;
            }
            TreeNode *newNode = new TreeNode(nums[maximum]);
            if(direction == "right"){
                node->right = newNode;
            } else if (direction == "left"){
                node->left = newNode;
            }
            // Left side of the array
            constructNodes(newNode, nums, start, maximum-1, "left");
            // Right side of the array
            int leng = nums.size();
            constructNodes(newNode, nums, maximum+1, end, "right");
        }
    }
    
    TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
        int leng = nums.size();
        int maximum = findMaxIndex(nums, 0, leng-1);
        
        TreeNode *start = new TreeNode(nums[maximum]);
        // Left side of the array
        constructNodes(start, nums, 0, maximum-1, "left");
        // Right side of the array
        constructNodes(start, nums, maximum+1, leng-1, "right");
        return start;
    }
};