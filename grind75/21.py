# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: 
Optional[ListNode]) -> Optional[ListNode]:
        
        def dfs(list1, list2):
            if not list1:
                return list2
            
            if not list2:
                return list1
            
            if list1.val < list2.val:
                list1.next = dfs(list1.next, list2)
                return list1

            else:
                list2.next = dfs(list2.next, list1)
                return list2
        
        return dfs(list1, list2)
