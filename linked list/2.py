# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    
    #converting input number to linked list
    def number2ll(self, num: int) -> ListNode:

        ll = ListNode()
        temp = ll
       
        while num >= 10:
            
            temp.val = num % 10
            temp.next = ListNode()
            temp = temp.next
            num = num//10
            
        temp.val = num
        return ll
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        
        result = 0
        multiplier = 1
        
        while l1 != None:
            
            result += multiplier * l1.val
            
            multiplier *= 10
            
            l1 = l1.next
        
        multiplier = 1
        
        while l2 != None:
            
            result += multiplier * l2.val
            
            multiplier *= 10
            
            l2 = l2.next        
            
        
        return self.number2ll(result)
 
            
        