# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        #time: O(n)
        #space: O(1)
        
        if not head or not head.next:
            return head
        
        previous = ListNode(head.val)
        while head.next:
            head = head.next
            new = ListNode(head.val)
            new.next = previous
            previous = new
            
        return new