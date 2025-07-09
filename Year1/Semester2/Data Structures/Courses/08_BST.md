# Binary Search Trees (BST)

## Motivation

A **Binary Search Tree (BST)** is a binary tree where each node satisfies the **BST property**:

> For any node `n`:
> - All keys in the left subtree are less than `n.key`
> - All keys in the right subtree are greater than `n.key`

BSTs allow:
- Fast search, insertion, and deletion (in average cases)
- Ordered traversal (in-order = sorted)
- Easy recursive implementation

---

## Node Structure

```pseudo
class Node:
    key
    left
    right
```

# Core Operations

| Operation | Description                        |
| --------- | ---------------------------------- |
| search(k) | Find a node with key `k`           |
| insert(k) | Add a new node with key `k`        |
| delete(k) | Remove node with key `k` (3 cases) |
| min()     | Find node with minimum key         |
| max()     | Find node with maximum key         |
| inOrder() | Traverse nodes in sorted order     |

# Complexity Summary

| Operation | Best Case | Average Case | Worst Case | Space |
| --------- | --------- | ------------ | ---------- | ----- |
| Search    | O(log n)  | O(log n)     | O(n)       | O(n)  |
| Insert    | O(log n)  | O(log n)     | O(n)       | O(n)  |
| Delete    | O(log n)  | O(log n)     | O(n)       | O(n)  |
| Traversal | O(n)      | O(n)         | O(n)       | O(n)  |
