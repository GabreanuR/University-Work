# AVL Tree

## Motivation

An **AVL tree** is a **self-balancing Binary Search Tree (BST)** where the height difference between left and right subtrees (called **balance factor**) is at most 1 for every node.

> Named after its inventors: Adelson-Velsky and Landis

This ensures **O(log n)** height, which guarantees efficient insertion, deletion, and search.

---

## Balance Factor

For each node:
- balanceFactor = height(left subtree) - height(right subtree)
- Valid range: **-1, 0, 1**
- If outside this range after an insertion or deletion, the tree must **rebalance** using **rotations**

---

## Rotations (to restore balance)

| Case             | When it Happens                 | Fix                   |
|------------------|---------------------------------|-----------------------|
| Left-Left (LL)   | Inserted in left-left subtree   | Single right rotation |
| Right-Right (RR) | Inserted in right-right subtree | Single left rotation  |
| Left-Right (LR)  | Inserted in left-right subtree  | Left rotation + Right |
| Right-Left (RL)  | Inserted in right-left subtree  | Right rotation + Left |

---

## Core Operations

| Operation    | Description                           |
|--------------|---------------------------------------|
| insert(x)    | Insert `x` and rebalance if necessary |
| delete(x)    | Delete `x` and rebalance if necessary |
| search(x)    | Check if `x` exists in the tree       |
| inorder()    | Sorted traversal of all nodes         |
| getBalance() | Get balance factor of a node          |

---

## Complexity Summary

| Operation | Time     | Space |
|-----------|----------|-------|
| Search    | O(log n) | O(n)  |
| Insert    | O(log n) | O(n)  |
| Delete    | O(log n) | O(n)  |

AVL trees maintain **strict height balancing**, making them slightly slower than unbalanced BSTs for insertion but **much more reliable in the long run**.

---

## Pseudocode Snippets (Insert with Rotation)

```pseudo
function insert(node, key):
    if node == null:
        return new Node(key)

    if key < node.value:
        node.left = insert(node.left, key)
    else if key > node.value:
        node.right = insert(node.right, key)
    else:
        return node  // duplicates not allowed

    updateHeight(node)
    balance = getBalance(node)

    // Left Left Case
    if balance > 1 and key < node.left.value:
        return rotateRight(node)

    // Right Right Case
    if balance < -1 and key > node.right.value:
        return rotateLeft(node)

    // Left Right Case
    if balance > 1 and key > node.left.value:
        node.left = rotateLeft(node.left)
        return rotateRight(node)

    // Right Left Case
    if balance < -1 and key < node.right.value:
        node.right = rotateRight(node.right)
        return rotateLeft(node)

    return node
```

# Key Characteristics
- Strictly balanced using rotations
- Each node stores its height
- Guaranteed O(log n) operations
- Slight overhead vs standard BST due to rotations

# Common Pitfalls
- Forgetting to update heights after rotations
- Not handling duplicate keys properly
- Mixing up rotation directions (LL vs LR etc.)
- Incorrect balance factor calculation

# Use Cases
- Memory-constrained systems needing guaranteed log-time access
- Databases or file indexes where balance is critical
- Scenarios where data is inserted/deleted frequently

# Related Structures
- [Heaps](12_Heaps.md) – for priority, not full ordering
- [Binary Search Tree](14_BST.md) – basic structure without balancing 
- [Splay Tree](16_Splay.md) – self-adjusting, not self-balancing
- [Red-Black Tree](17_RedBlack.md) – more relaxed balancing rules
