/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    private int left = 0;
    private int right = 0;
    private int savedL = 0;
    private int savedR = 0;
    private int totalTilt = 0;
    
    public void recurseAdd(TreeNode node){
        // Go to all of the children and find the values
        if(node.left != null){
            recurseAdd(node.left);
            left += node.left.val;
        }
        if(node.right != null){
            recurseAdd(node.right);
            right += node.right.val;
        }
        // After finding all children and adding to the counter
        totalTilt += Math.abs(left - right);
    }

    public int findTilt(TreeNode root) {
        if(root == null){
            return 0;
        }
        if(root.left != null){
            recurseAdd(root.left);
            savedL = left + right;
            left = 0;
            right = 0;
        }
        System.out.println(totalTilt);
        if(root.right != null){
            recurseAdd(root.right);
            savedR = left + right;
        }
        System.out.println(totalTilt);
        // Calculate the root tilt using the previous values
        left = savedL;
        right = savedR;
        if(root.left != null){
            left += root.left.val;
        }
        if(root.right != null){
            right += root.right.val;
        }
        System.out.println(left);
        System.out.println(right);
        totalTilt += Math.abs(left - right);
        // Add the top node
        // totalTilt += recurseRoot(root);
        return totalTilt;
    }
}