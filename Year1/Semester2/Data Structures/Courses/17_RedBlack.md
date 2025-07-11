# Red-Black Tree

## Motivation

A **Red-Black Tree** is a type of **self-balancing Binary Search Tree (BST)** that ensures the tree height is always `O(log n)` by enforcing **coloring rules**.

Compared to AVL trees:
- Slightly **less strictly balanced**
- **Faster insertions/deletions** in practice
- Used in real-world libraries (e.g., C++ `std::map`, Java `TreeMap`)

---

## Red-Black Properties

Every Red-Black Tree satisfies these **5 rules**:

1. Each node is either **red** or **black**
2. The **root is black**
3. **All leaves (NILs) are black**
4. Red nodes cannot have red children (no two reds in a row)
5. Every path from a node to its descendant NILs contains the **same number of black nodes** (black-height)

These rules ensure that the longest path is no more than **twice** as long as the shortest → keeps the height balanced.

---

## Rotations and Fix-ups

After an insertion or deletion, the tree may violate rules and must be **fixed** using:

- **Recoloring**
- **Left or right rotations**
- **Combinations of both**

There are several **cases** depending on:
- Color of parent, uncle, and grandparent
- Tree shape (left/right, zig/zag)

---

## Core Operations

| Operation | Description                                         |
|-----------|-----------------------------------------------------|
| insert(x) | Insert and then fix violations via rotation/recolor |
| delete(x) | Delete and rebalance if red-black properties break  |
| search(x) | Standard BST search                                 |
| inorder() | Traverse in sorted order                            |

---

## Complexity Summary

| Operation | Time     | Space |
|-----------|----------|-------|
| Search    | O(log n) | O(n)  |
| Insert    | O(log n) | O(n)  |
| Delete    | O(log n) | O(n)  |

> Height is guaranteed to be `≤ 2 * log₂(n+1)`  
> This is slightly taller than AVL but still logarithmic.

---

## Simplified Pseudocode (Insert with Fix)

```pseudo
function insert(root, x):
    node = standardBSTInsert(root, x)
    node.color = RED
    fixInsert(root, node)

function fixInsert(root, node):
    while node ≠ root and node.parent.color == RED:
        if node.parent is left child:
            uncle = node's grandparent.right
            if uncle.color == RED:
                // case 1: recolor
                parent.color = BLACK
                uncle.color = BLACK
                grandparent.color = RED
                node = grandparent
            else:
                if node is right child:
                    // case 2: rotate left
                    node = node.parent
                    rotateLeft(node)
                // case 3: rotate right
                node.parent.color = BLACK
                node.grandparent.color = RED
                rotateRight(node.grandparent)
        else:
            // mirror case
            ...
    root.color = BLACK
```

# Key Characteristics
- All operations run in O(log n) time
- Automatically balanced through coloring and rotations
- Great performance for insertion-heavy workloads
- Common in library implementations (e.g., STL, TreeMap)

# Common Pitfalls
- Forgetting to recolor correctly
- Misapplying rotations (especially mirrored cases)
- Confusing leaf nodes with "null" pointers (NILs)
- Overcomplicating logic—keep case distinction clear

# Use Cases
- Language libraries: std::map, std::set, Java TreeMap
- Symbol tables in compilers
- Memory allocators
- Associative containers (maps/dictionaries) with ordering

# Related Structures
- [Heaps](12_Heaps.md) – priority-based, not ordered
- [Binary Search Tree](14_BST.md) – no balancing
- [AVL Tree](15_AVL.md) – stricter balancing via height
- [Splay Tree](16_Splay.md) – self-adjusts on access