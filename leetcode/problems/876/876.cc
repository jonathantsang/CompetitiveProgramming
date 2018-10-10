/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        int length = 0;
        ListNode *node = head;
        while(node){
            length++;
            node = node->next;
        }
        int mid = length / 2; // This gets the middle number 4->2 5->2
        // As if it was zero indexed
        node = head;
        int i = 0;
        while(i < mid){
            node = node->next;
            i++;
        }
        return node;
    }
};