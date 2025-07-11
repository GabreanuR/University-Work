# Singly Linked Lists (SLL)

## Motivation

A **singly linked list** is a linear data structure where each element (called a node) contains:
- A **value**
- A **pointer to the next node**

Unlike arrays, the elements are stored in **non-contiguous memory**, and you can dynamically grow or shrink the list.

Useful when:
- You need frequent insertions/deletions at the front or middle
- You want to avoid reallocations or memory shifts
- The number of elements is not known in advance

---

## Core Operations

| Operation      | Description                          |
|----------------|--------------------------------------|
| insertFront(x) | Add node with value `x` at the front |
| insertEnd(x)   | Add node at the end                  |
| insertAt(i, x) | Add node at index `i`                |
| deleteAt(i)    | Remove node at index `i`             |
| search(x)      | Check if value `x` exists            |
| traverse()     | Print or collect all elements        |

---

## Complexity Summary

| Operation     | Best Case | Average Case | Worst Case | Space |
|---------------|-----------|--------------|------------|-------|
| Access        | O(1)\*    | O(n)         | O(n)       | O(n)  |
| Search        | O(1)\*    | O(n)         | O(n)       | O(n)  |
| Insert front  | O(1)      | O(1)         | O(1)       | O(n)  |
| Insert end    | O(1)\*\*  | O(n)         | O(n)       | O(n)  |
| Delete front  | O(1)      | O(1)         | O(1)       | O(n)  |
| Delete middle | O(n)      | O(n)         | O(n)       | O(n)  |

> \* Only if you already have a pointer to the node  
> \*\* Only if you maintain a tail pointer

---

## Pseudocode Examples

### Node structure & insert at front

```pseudo
class Node:
    data
    next

function insertFront(head, x):
    newNode = Node(x)
    newNode.next = head
    head = newNode

function deleteAt(head, index):
    if index == 0:
        head = head.next
        return
    curr = head
    for i from 0 to index - 2:
        if curr == null:
            return "Index out of bounds"
        curr = curr.next
    curr.next = curr.next.next
```

# Key Characteristics
- Dynamic memory allocation (no fixed size)
- Elements linked via pointers, not contiguous
- Fast insertions and deletions at the front
- Requires traversal to access arbitrary elements
- Easily extensible into other list types (doubly, circular)

# Common Pitfalls
- Forgetting to update head pointer
- Memory leaks (if you forget to deallocate removed nodes)
- Dereferencing null pointers
- Infinite loops if next pointers are not correctly maintained

# Use Cases
- Stack and queue implementations
- Hash table chaining (collision resolution)
- Real-time systems with deterministic allocation
- Undo/Redo functionality

# Related Structures
- [Arrays](01_Arrays.md) – for random access
- [Vectors](02_Vectors.md) – dynamic but contiguous
- [Stacks](03_Stacks.md) – can be implemented with SLL
- [Doubly Linked List](07_DoublyLinkedLists.md) – allows bidirectional traversal
- [Circular Linked List](08_CircularLinkedLists.md) – tail connects back to head
- [Skip Lists](09_SkipLists.md) - allows fast search, insertion, and deletion operations