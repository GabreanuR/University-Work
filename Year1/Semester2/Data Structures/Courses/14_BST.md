# Binary Search Tree (BST)

## Motivation

A **Binary Search Tree (BST)** is a binary tree where every node satisfies the **BST property**:

> For every node `N`:
> - All values in the left subtree are **less than** `N`
> - All values in the right subtree are **greater than** `N`

BSTs allow efficient **search, insertion, and deletion** in `O(log n)` time if the tree is balanced.

---

## Core Operations

| Operation      | Description                                 |
|----------------|---------------------------------------------|
| insert(x)      | Add value `x` while preserving BST property |
| delete(x)      | Remove value `x` if it exists               |
| search(x)      | Check if value `x` exists in the tree       |
| inorder()      | Traverse in sorted order                    |
| min()/max()    | Return smallest/largest element             |

---

## Complexity Summary

| Operation | Best Case | Average  | Worst Case | Space |
|-----------|-----------|----------|------------|-------|
| Search    | O(log n)  | O(log n) | O(n)       | O(n)  |
| Insert    | O(log n)  | O(log n) | O(n)       | O(n)  |
| Delete    | O(log n)  | O(log n) | O(n)       | O(n)  |
| Traversal | O(n)      | O(n)     | O(n)       | O(n)  |

> Worst case occurs when tree becomes skewed (degenerates into a list). Use AVL or Red-Black trees to maintain balance.

---

## Pseudocode Example (Recursive Insert & Search)

```pseudo
function insert(node, x):
    if node == null:
        return new Node(x)
    if x < node.value:
        node.left = insert(node.left, x)
    else if x > node.value:
        node.right = insert(node.right, x)
    return node

function search(node, x):
    if node == null:
        return false
    if x == node.value:
        return true
    else if x < node.value:
        return search(node.left, x)
    else:
        return search(node.right, x)
```

# Key Characteristics
- Each node has at most two children
- Maintains sorted order of elements
- Allows efficient range queries
- Traversal in-order gives sorted sequence
- Performance depends heavily on balance

# Common Pitfalls
- Not handling duplicates (BSTs often disallow them)
- Forgetting to update parent pointers when deleting
- Tree becoming unbalanced → O(n) performance
- Incorrect recursive base cases

# Use Cases
- Symbol tables and dictionaries
- Range queries and interval trees
- Auto-complete systems (with prefixes stored as keys)
- Data storage where sorted order matters

# Related Structures
- [Arrays](01_Arrays.md) – better for binary search if data is static
- [Heaps](12_Heaps.md) – prioritize max/min, not full ordering
- [AVL Tree](15_AVL.md) – self-balancing BST with height difference ≤ 1
- [Splay Tree](16_Splay.md) – self-adjusting BST with access optimization
- [Red-Black Tree](17_RedBlack.md) – balanced BST with coloring rules