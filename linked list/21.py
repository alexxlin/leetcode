# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        #corner cases
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        result = ListNode()
        temp_pointer = result
        
        first = l1
        second = l2
        
        result.val = min(l1.val, l2.val)
        
        while (l1 != None or l2 != None):
            
            if l2 == None or (l1 != None and l2 != None and l1.val < l2.val):
                temp_pointer.next = l1
                l1 = l1.next
                temp_pointer = temp_pointer.next
            
            else:
                temp_pointer.next = l2
                l2 = l2.next
                temp_pointer = temp_pointer.next
        
        return result.next