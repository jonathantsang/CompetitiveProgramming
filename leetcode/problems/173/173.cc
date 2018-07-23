/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class BSTIterator {
    vector<TreeNode *> stack;
    
    void traverse(TreeNode *node){
        while(node){
            stack.push_back(node);
            node = node->left;
        }
    }
    
public:
    BSTIterator(TreeNode *root) {
        // traverse the bst
        traverse(root);
    }

    /** @return whether we have a next smallest number */
    bool hasNext() {
        return !stack.empty();
    }

    /** @return the next smallest number */
    int next() {
        int v = stack.back()->val;
        TreeNode *back = stack.back();
        stack.pop_back();
        if(back->right){
            back = back->right;
            while(back){
                stack.push_back(back);
                back = back->left;
            }
        }
        return v;
    }
};

/**
 * Your BSTIterator will be called like this:
 * BSTIterator i = BSTIterator(root);
 * while (i.hasNext()) cout << i.next();
 */