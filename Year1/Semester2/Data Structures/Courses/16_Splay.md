# Splay Tree

## Motivation

A **Splay Tree** is a type of **self-adjusting Binary Search Tree (BST)** where **recently accessed elements are moved to the root** via a process called **splaying**.

This improves performance for:
- Elements accessed frequently
- Sequences with temporal locality (repeated access to nearby nodes)

---

## Splaying Operation

**Splaying** = moving a node to the root using rotations.

### Three main cases during splay:

| Case    | Description                                 | Action                                 |
|---------|---------------------------------------------|----------------------------------------|
| Zig     | Node is child of root                       | Single rotation                        |
| Zig-Zig | Node and parent are both left or both right | Double rotation in same direction      |
| Zig-Zag | Node and parent are opposite sides          | Double rotation in opposite directions |

---

## Core Operations

| Operation     | Description                                 |
|---------------|---------------------------------------------|
| search(x)     | Search `x` and splay it to root             |
| insert(x)     | Insert `x`, then splay it to root           |
| delete(x)     | Splay `x` to root, then remove it           |
| splay(x)      | Internal helper: bring `x` to the root      |
| inorder()     | Print sorted elements                       |

---

## Complexity Summary

| Operation | Amortized Time | Worst Case | Space |
|-----------|----------------|------------|-------|
| Search    | O(log n)       | O(n)       | O(n)  |
| Insert    | O(log n)       | O(n)       | O(n)  |
| Delete    | O(log n)       | O(n)       | O(n)  |
| Splay     | O(log n)       | O(n)       | O(n)  |

> Time complexity is **amortized** — over many operations, average is O(log n), even if some are O(n)

---

## Pseudocode – Simplified Splay Step

```pseudo
function splay(node, key):
    if node is null or node.key == key:
        return node

    if key < node.key:
        if node.left == null:
            return node
        if key < node.left.key:
            node.left.left = splay(node.left.left, key)
            node = rotateRight(node)
        else if key > node.left.key:
            node.left.right = splay(node.left.right, key)
            if node.left.right != null:
                node.left = rotateLeft(node.left)
        return node.left == null ? node : rotateRight(node)
    else:
        if node.right == null:
            return node
        if key > node.right.key:
            node.right.right = splay(node.right.right, key)
            node = rotateLeft(node)
        else if key < node.right.key:
            node.right.left = splay(node.right.left, key)
            if node.right.left != null:
                node.right = rotateRight(node.right)
        return node.right == null ? node : rotateLeft(node)
```

# Key Characteristics
- Frequently accessed elements become faster over time
- No balance factor or color: structure changes via access pattern
- Very simple structure (only rotations, no metadata)
- Good for working sets and temporal locality

# Common Pitfalls
- Assuming guaranteed log-time for each operation (only amortized)
- Forgetting to splay after search/insert/delete
- Harder to visualize and debug than AVL or Red-Black
- Doesn't prevent degeneration in worst-case patterns

# Use Cases
- Caches with temporal locality
- Simple memory allocators
- Implementing access-optimized maps/sets
- Real-time systems where recent access matters more than strict balance

# Related Structures
- [Heaps](12_Heaps.md) – not sorted, but for priorities
- [Binary Search Tree](14_BST.md) – basic tree structure
- [AVL Tree](15_AVL.md) – strict self-balancing tree
- [Red-Black Tree](17_RedBlack.md) – balanced with color rules