# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        # import copy
        #1. recursion each time finding the smallest node
        #DOESN'T WORK, can make shallow copy of ll in smallest
        
        #keeps track of linked list with smallest head value
#         smallest = None

#         for i in range(len(lists)):
#             if (not smallest) or (lists[i] and lists[i].val < smallest.val):
#                 smallest = lists[i]

#         if smallest:
#             head = ListNode(smallest.val)
#             smallest = smallest.next
#             head.next = self.mergeKLists(lists)

#         return head

        #2. merge two lists at a time
        #to optimize it, merge two different lists each time (divide and conquer)
        #instead of always merging first two lists
        
        #time: O(n * k) k linked lists, n nodes per list
        #space: O(n log k) recursive stacks
        

        def merge(list1, list2):
            
            if not list1:
                return list2
            
            if not list2:
                return list1
            
            head = temp = ListNode(0)
            
            while list1 and list2:
    
                if list1.val <= list2.val:
                    temp.next = list1
                    list1 = list1.next

                else:
                    temp.next = list2
                    list2 = list2.next

                temp = temp.next
            
            if list1:
                temp.next = list1
                
            if list2:
                temp.next = list2
                
            return head.next
            
        
        k = len(lists)
        
        if k == 0:
            return None

        interval = 1
        
        
        while interval < k:    
            for i in range(0, k - interval, interval * 2):
                lists[i] = merge(lists[i], lists[i + interval])
            interval *= 2
            
            
        return lists[0]
    
        
            

    
    