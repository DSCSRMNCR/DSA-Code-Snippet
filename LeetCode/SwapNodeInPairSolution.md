# Swap Two Nodes In Pair
Link- https://leetcode.com/problems/swap-nodes-in-pairs/

Explaination- Uses Inbuilt swap function to swap to node then the pointer is incremented twice till it points to NULL
Example- For input head = [1,2,3,4]
Algorithm
1.Node p is poiting towards head of the Linked List
2.Two pair p and its next are swap
3.Pointer p is incremented twice
4.This loop goes on till p and its next is not NULL

## code

'''CPP
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
'''

## Output

'''
[2,1,4,3]
'''

## Contributed By
| Name | GitHub username | Institute |
|--|--|--|
| Nutan Tupe | [Nutan2305](https://github.com/Nutan2305) | Cummins College of Engineering, Pune |
