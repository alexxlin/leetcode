/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Neighbors []*Node
 * }
 */

func cloneGraph(node *Node) *Node {
    if node == nil { return nil }
    m := make(map[*Node]*Node)
    visited := make(map[int]struct{})

    stack := []*Node{node}
    visited[node.Val] = struct{}{}
    for len(stack) > 0 {
        node := stack[len(stack)-1]
        stack = stack[:len(stack)-1]
        m[node] = &Node{Val: node.Val}
        for _, n := range node.Neighbors {
            if _, ok := visited[n.Val]; ok { continue }
            stack = append(stack, n)
            visited[n.Val] = struct{}{}
        }
    }
    for on, nn := range m {
        nn.Neighbors = []*Node{}
        for _, one := range on.Neighbors {
            nn.Neighbors = append(nn.Neighbors, m[one])
        }
    }
    return m[node]
}
