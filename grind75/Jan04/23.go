/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeKLists(lists []*ListNode) *ListNode {
    if len(lists) == 0 {
        return nil
    }
    if len(lists) == 1 {
        return lists[0]
    }
    m := (len(lists)/2)
    l := mergeKLists(lists[:m])
    r := mergeKLists(lists[m:])
    return mergeLists(l, r)

}

func mergeLists(a, b *ListNode) *ListNode {
    cur := &ListNode{}
    prev := cur

    for a != nil && b != nil {
        if a.Val < b.Val {
            cur.Next = a
            a = a.Next
        } else {
            cur.Next = b
            b = b.Next
        }
        cur = cur.Next
    }

    if a != nil {
        cur.Next = a
    }
    if b != nil {
        cur.Next = b
    }
    return prev.Next
}
