/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool helper(TreeNode* root, long minval, long maxval) {
        if (!root) { return true; }
        if (root->val <= minval || root->val >= maxval) {
            return false;
        }
        return helper(root->left, minval, root->val) && helper(root->right, root->val, maxval);
    }


    bool isValidBST(TreeNode* root) {
        if (!root) { return true; }
        return helper(root->left, LONG_MIN, root->val) && helper(root->right, root->val, LONG_MAX);
    }
};