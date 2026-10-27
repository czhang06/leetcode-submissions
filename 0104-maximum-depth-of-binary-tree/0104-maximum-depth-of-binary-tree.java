/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int maxDepth(TreeNode root) {
        Queue<TreeNode> nodeq = new ArrayDeque<>();
        Queue<Integer> depthq = new ArrayDeque<>();

        int result = 0;

        if (root == null) return 0;
        nodeq.offer(root);
        depthq.offer(1);
        while (!nodeq.isEmpty()) {
            TreeNode node = nodeq.poll();
            int depth = depthq.poll();
            result = Math.max(result, depth);
            if (node.left != null)  { nodeq.offer(node.left);  depthq.offer(depth + 1); }
            if (node.right != null) { nodeq.offer(node.right); depthq.offer(depth + 1); }
        }

        return result;
    }
}