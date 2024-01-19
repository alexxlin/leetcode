/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeNthFromEnd(head *ListNode, n int) *ListNode {
    fast := head
    for n > 0 {
        fast = fast.Next
        n--
    }
    prev := &ListNode{}
    slow := head

    for fast != nil {
        prev = slow
        slow = slow.Next
        fast = fast.Next
    }
    if slow == head {
        return head.Next
    }
    prev.Next = slow.Next
    slow = nil
    return head
}
