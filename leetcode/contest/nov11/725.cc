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
    vector<ListNode*> splitListToParts(ListNode* root, int k) {
        int length  = 0;
        ListNode *node = root;
        vector<ListNode *> final;
        vector<ListNode *> values;
        while(node != nullptr){
            length++;
            values.emplace_back(node);
            node = node->next;
        }
        // Each one is lengEach size, with remainder being larger by 1
        int lengEach = length / k;
        int longerone = lengEach+1;
        int remainder = length % k;
        int index = 0;
        //cout << lengEach << " " << longerone << " " << remainder << endl;
        for(int i = 0; i < remainder; i++){
            final.emplace_back(values[index]);
            // Cut off last one in chain
            values[index+longerone-1]->next = nullptr;
            index = index + longerone;
            if(index > length){
                // ? shouldn't do this
                break;
            }
        }
        
        if(length < k){
            int rest = k - remainder;
            for(int i = 0; i < rest; i++){
                final.emplace_back(nullptr);
            }
            return final;
        }        
        int start = remainder * (lengEach + 1);
        int amtLeft = k - remainder;
        //cout << start << " " << amtLeft << endl;
        for(int i = 0; i < amtLeft; i++){
            //cout << values[start]->val << endl;
            final.emplace_back(values[start]);
            values[start+lengEach-1]->next = nullptr;
            start = start + lengEach;
            if(start >= length){
                break;
            }
        }
        return final;
    }
};