# Linked Lists

## Motivation

A **linked list** is a linear data structure where elements (nodes) are stored in **non-contiguous** memory locations, each pointing to the next (and possibly previous) node.

Linked lists are useful when:
- You need frequent insertions/deletions anywhere in the list
- You don’t know the number of elements in advance
- You want to avoid reallocations and shifting (like in arrays)

---

## Types of Linked Lists

| Type                   | Description                                 |
|------------------------|---------------------------------------------|
| Singly Linked List     | Each node has a pointer to the next node    |
| Doubly Linked List     | Each node has pointers to both next & prev  |
| Circular Linked List   | Last node points to the first node          |

---

## Core Operations (SLL)

| Operation        | Description                           |
|------------------|---------------------------------------|
| insertFront(x)   | Add at beginning                      |
| insertEnd(x)     | Add at end                            |
| insertAt(i, x)   | Add at index `i`                      |
| deleteAt(i)      | Remove node at index `i`              |
| search(x)        | Check if value exists                 |
| traverse()       | Print all elements                    |

---

## Complexity Summary

### Singly Linked List

| Operation     | Best Case | Average | Worst Case | Space |
|---------------|-----------|---------|------------|--------|
| Access        | O(1)*     | O(n)    | O(n)       | O(n)   |
| Search        | O(1)*     | O(n)    | O(n)       | O(n)   |
| Insert front  | O(1)      | O(1)    | O(1)       | O(n)   |
| Insert end    | O(1)**    | O(n)    | O(n)       | O(n)   |
| Delete front  | O(1)      | O(1)    | O(1)       | O(n)   |
| Delete middle | O(n)      | O(n)    | O(n)       | O(n)   |

> \* O(1) if node pointer is already known  
> \** O(1) if you maintain a tail pointer

---

## Pseudocode Examples (Singly Linked List)

### Node Structure

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
- No contiguous memory required
- Poor random access (must traverse)
- Great for insertions/deletions (especially at front)

# Common Pitfalls
- Memory leaks (not deleting nodes)
- Forgetting to update head/tail pointers
- Null pointer dereferencing
- Infinite loops in circular lists

# Use Cases
- Implementation of stacks, queues, hash tables (chaining)
- Undo/Redo functionality
- Adjacency lists in graph representations
- Real-time systems (deterministic insert/delete)
