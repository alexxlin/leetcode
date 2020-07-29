# Definition for singly-linked list.
# class ListNode
#     def __init__(self, val=0, next=None)
#         self.val = val
#         self.next = next
class Solution
    def reorderList(self, head ListNode) - None
        
        Do not return anything, modify head in-place instead.
        
        
        #time O(n)
        #space O(1)
        
        #1. find middle point of linked list (#876)
        #2. reverse second linked list (#206)
        #3. merge the two linked list, one by one (#21)
        
        if not head
            return head
        
        #1.
        fast = slow = head
        
        while fast and fast.next
            slow = slow.next
            fast = fast.next.next
        
        
        #2. using two pointers and a temp to store current.next
        #each iteration shifting by one
        previous = None
        current = slow
        
        while current
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        
        #3. using temp to store firstsecond.next
        #each iteration has two merging
        first = head
        second = previous
        
        while second.next
            
            temp = first.next
            first.next = second
            first = temp
            
            temp = second.next
            second.next = first
            second = temp
            
        return head
            
        
        
        
        
        
        