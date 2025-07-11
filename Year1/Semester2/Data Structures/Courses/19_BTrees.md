# B-Trees

## Motivation

A **B-Tree** is a self-balancing generalization of binary search trees (BST), optimized for **storage systems** (like disks or databases).

It maintains sorted data and allows:
- Efficient **search**, **insertion**, **deletion**
- All in **logarithmic time**, even for very large datasets

> Used in: databases (MySQL, PostgreSQL), file systems (NTFS, HFS+), indexing systems

---

## Key Properties (B-Tree of order *t*)

- Every node has at most **2t - 1 keys** and **2t children**
- Every node (except root) has at least **t - 1 keys**
- All leaves are at the **same depth**
- Keys in a node are kept **sorted**
- Internal nodes guide the search using key intervals
- Height is kept low → efficient disk access

---

## Operations

### Search

Works like in BST, but at each node:
- Use **binary search** to find the correct child
- Go down recursively

### Insert

- Insert like in BST (top-down), but:
- If a node becomes full → **split** it
- Splits may propagate up to the root (may grow tree height)

### Delete

- More complex than in BST
- Ensure nodes always have at least **t-1 keys**
- May involve **borrowing** from siblings or **merging** nodes

---

## Complexity

| Operation | Time     | Space |
|-----------|----------|-------|
| Search    | O(log n) | O(n)  |
| Insert    | O(log n) | O(n)  |
| Delete    | O(log n) | O(n)  |

> Height of B-Tree is `O(logₜ n)` where `t` is the minimum degree

---

## Pseudocode – Simplified Insertion

```pseudo
function insert(T, key):
    if root is full:
        s = new empty node
        s.children[0] = T.root
        splitChild(s, 0)
        insertNonFull(s, key)
        T.root = s
    else:
        insertNonFull(T.root, key)

function insertNonFull(x, key):
    if x is a leaf:
        insert key into x.keys in sorted order
    else:
        i = index to insert key
        if x.children[i] is full:
            splitChild(x, i)
            if key > x.keys[i]:
                i += 1
        insertNonFull(x.children[i], key)

function splitChild(parent, i):
    y = parent.children[i]
    z = new node
    z.keys = y.keys[t to 2t - 2]
    if not leaf:
        z.children = y.children[t to 2t - 1]
    y.keys = y.keys[0 to t - 2]
    parent.insertKeyAt(i, y.keys[t - 1])
    parent.insertChildAt(i + 1, z)
```

# Advantages
- Low height → fewer disk accesses
- Good for systems where reading from disk is expensive
- Balanced without needing many rotations

# Common Pitfalls
- Forgetting to split before descending
- Mishandling edge cases when deleting from root
- Not maintaining sorted keys inside nodes
- Assuming B-Tree is binary (it’s not)

# Use Cases
- Database indexes (MySQL's InnoDB uses B+ Trees)
- File systems (NTFS, HFS+, ext4 indirect blocks)
- Key-value stores (e.g., LevelDB, RocksDB)
- Large sorted sets of data on disk

# Related Structures
- [Heaps](12_Heaps.md) – for priority, not ordered
- [Binary Search Tree](14_BST.md) – basic structure, not disk-friendly
- [AVL Tree](15_AVL.md) – balanced BST with stricter balancing
- [Red-Black Tree](17_RedBlack.md) – balanced BST used in memory
- [Tries](21_Tries.md) – prefix trees for string keys