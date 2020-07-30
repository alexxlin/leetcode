# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        #1. recursion
        
        #time: O(n + m)
        #space: O(n + m)
            
#         if l1 == None:
#             return l2

#         if l2 == None:
#             return l1

#         if l1.val <= l2.val:
#             l1.next = self.mergeTwoLists(l1.next, l2)
#             return l1

#         else:
#             l2.next = self.mergeTwoLists(l1, l2.next)
#             return l2

        #2. iteration
        
        #time: O(n+m)
        #space: O(n + m) creating a new list

            if l1 == None:
                return l2
            
            if l2 == None:
                return l1
            
            head = temp = ListNode(0)
            
            while l1 and l2:
            
                if l1.val <= l2.val:
                    temp.next = l1
                    l1 = l1.next

                else:
                    temp.next = l2
                    l2 = l2.next
                
                temp = temp.next
                    
            if l1:
                temp.next = l1
                
            if l2:
                temp.next = l2
                
            return head.next
                
        
            
                