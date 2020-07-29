# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        
        #time: O(n)
        #space: O(1)
        
        #actually smarter to use fast and slow pointer
        
        if not head:
            return head
        
        count, temp = 0, head
        while temp:
            temp = temp.next
            count += 1
        
        mid = math.ceil((count + 1) / 2)
        
        temp = head
        while mid > 1:
            temp = temp.next
            mid -= 1
        
        return temp
            
            