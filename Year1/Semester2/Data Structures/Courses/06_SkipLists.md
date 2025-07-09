# Skip Lists

## Motivation

A **Skip List** is a probabilistic data structure that allows fast search, insertion, and deletion operations — similar to balanced binary search trees — but uses multiple levels of linked lists.

It is useful when:
- You want **logarithmic time** for search, insert, and delete
- You prefer **simpler implementation** over self-balancing trees (e.g., AVL, Red-Black Trees)
- You want a **dynamic sorted structure** with low overhead

---

## Core Idea

A skip list augments a sorted singly linked list with additional forward pointers at **multiple levels**:

- Level 0 → normal sorted list
- Level 1 → skips 2 nodes at a time
- Level 2 → skips 4 nodes, etc.

This layered structure allows **fast skipping** over irrelevant elements during search.

---

## Core Operations

| Operation   | Description                          |
|-------------|--------------------------------------|
| search(x)   | Locate element `x`                   |
| insert(x)   | Add element `x` in sorted position   |
| delete(x)   | Remove element `x` if it exists      |

---

## Complexity Summary

| Operation   | Best Case | Average Case | Worst Case | Space Complexity |
|-------------|-----------|--------------|-------------|-------------------|
| Search      | O(1)      | O(log n)     | O(n)        | O(n log n)        |
| Insert      | O(1)      | O(log n)     | O(n)        | O(n log n)        |
| Delete      | O(1)      | O(log n)     | O(n)        | O(n log n)        |

> Worst case occurs if random level assignment fails badly (rare).  
> Average case is expected with good probabilistic balance (p = 0.5).

---

## Pseudocode (Search & Insert)

### Node Structure

```pseudo
class Node:
    value
    forward[]  # Array of pointers to next nodes on each level

function search(x):
    curr = head
    for i from level downto 0:
        while curr.forward[i] != null and curr.forward[i].value < x:
            curr = curr.forward[i]
    curr = curr.forward[0]
    if curr != null and curr.value == x:
        return true
    return false

function insert(x):
    update[] = new array[level+1]
    curr = head
    for i from level downto 0:
        while curr.forward[i] != null and curr.forward[i].value < x:
            curr = curr.forward[i]
        update[i] = curr

    newLevel = randomLevel()
    if newLevel > level:
        for i from level+1 to newLevel:
            update[i] = head
        level = newLevel

    newNode = Node(x)
    for i from 0 to newLevel:
        newNode.forward[i] = update[i].forward[i]
        update[i].forward[i] = newNode
```

# Common Pitfalls
- Not initializing head with maximum level
- Forgetting to update all levels during insertion or deletion
- Not using a consistent random level generator (geometric distribution)

# Random Level Generator

```pseudo
function randomLevel():
    level = 0
    while rand() < p and level < MAX_LEVEL:
        level += 1
    return level
```

Common choices:
- p = 0.5 or 1/e
- MAX_LEVEL ≈ log₂(n) or fixed constant (e.g. 16 or 32)

# Use Cases
- Sorted associative containers (alternative to trees)
- Indexing in databases or memory-constrained systems
- Concurrent-friendly variants in lock-free data structures

# Related Structures
- [Binary Search Trees](./08_BST.md) – similar performance, more deterministic
- [Hash Tables](./07_HashTables.md) – faster on average, but unordered
- [Arrays](./01_Arrays.md) – better cache performance, but no fast insertion
