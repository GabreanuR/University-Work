# Trees – Introduction

## What is a Tree?

A **tree** is a hierarchical data structure consisting of **nodes** connected by **edges**, with the following properties:
- One special node called the **root**
- Each node may have **zero or more children**
- There are **no cycles** (i.e., it’s a connected acyclic graph)

---

## Terminology

| Term        | Description                                       |
|-------------|---------------------------------------------------|
| Root        | The top-most node of the tree                     |
| Leaf        | A node with no children                           |
| Parent      | A node directly above another node                |
| Child       | A node directly below another node                |
| Sibling     | Nodes with the same parent                        |
| Height      | Longest path from a node to a leaf                |
| Depth       | Distance from the root to a given node            |
| Subtree     | A tree formed from a node and its descendants     |
| Degree      | Number of children a node has                     |

---

## Binary Trees

A **binary tree** is a tree where:
- Each node has **at most two children**
- These children are commonly referred to as **left** and **right**

---

## Types of Binary Trees

| Type                 | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| Full Binary Tree     | Every node has 0 or 2 children                                              |
| Perfect Binary Tree  | All internal nodes have 2 children and all leaves are at the same depth     |
| Complete Binary Tree | All levels are completely filled, except possibly the last (left-filled)    |
| Balanced Binary Tree | Height is `O(log n)` for `n` nodes (balance depends on implementation)      |

---

## Tree Traversals

Tree traversal = visiting all nodes in a specific order.

### Depth-First Traversal

| Type      | Order                         |
|-----------|-------------------------------|
| Inorder   | Left → Root → Right           |
| Preorder  | Root → Left → Right           |
| Postorder | Left → Right → Root           |

### Breadth-First Traversal (Level Order)

- Visit nodes level by level using a queue (BFS)

---

## Representation in Memory

- **Pointer-based**: Each node stores pointers to its children
- **Array-based** (used for complete trees like heaps):
    - Node at index `i`:
        - Left child: `2i + 1`
        - Right child: `2i + 2`
        - Parent: `(i - 1) // 2`

---

## Common Pitfalls

- Confusing depth and height
- Off-by-one indexing in array representation
- Forgetting to handle null pointers in recursive traversals

---

## Use Cases

- Hierarchical data (file systems, org charts)
- Parsers and expression trees (compilers)
- Binary Search Trees (BSTs)
- Heaps and priority queues
- Segment trees and range queries

---

## Related Structures
- [Heaps](12_Heaps.md) – complete tree for priority queues (max/min root)
- [Binary Search Tree](14_BST.md) – sorted binary tree with O(log n) operations
- [AVL Tree](09_AVL.md) – self-balancing BST with strict height balancing
- [Splay Tree](10_Splay.md) – self-adjusting BST with recently-used access boost
- [Red-Black Tree](11_RedBlack.md) – balanced BST with red/black coloring rules


