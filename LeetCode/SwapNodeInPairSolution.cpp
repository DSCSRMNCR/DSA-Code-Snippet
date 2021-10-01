// leetcode problem solution for swap two nodes in pair
class Solution
{
public:
    ListNode *swapPairs(ListNode *head)
    {
        ListNode *p = head;
        while (p != NULL && p->next != NULL)
        {
            swap(p->val, p->next->val);
            p = p->next->next;
        }
        return head;
    }
};