# Doubly Linked Lists (DLL)

## Motivation

A **doubly linked list** is a linear data structure where each node stores:
- A **value**
- A pointer to the **next** node
- A pointer to the **previous** node

This allows **bidirectional traversal** and easier insertions/deletions at both ends or in the middle.

Useful when:
- You need to traverse both forward and backward
- You want efficient insertion/removal at both ends
- You want to quickly remove a node if you have its pointer

---

## Core Operations

| Operation         | Description                           |
|-------------------|---------------------------------------|
| insertFront(x)    | Insert node at the beginning          |
| insertEnd(x)      | Insert node at the end                |
| deleteFront()     | Remove the first node                 |
| deleteEnd()       | Remove the last node                  |
| insertAfter(p, x) | Insert node after a given pointer `p` |
| delete(p)         | Delete node `p` when pointer is known |
| traverse()        | Traverse from head to tail            |
| reverseTraverse() | Traverse from tail to head            |

---

## Complexity Summary

| Operation         | Best Case | Average | Worst Case | Space |
|-------------------|-----------|---------|------------|-------|
| Access (by index) | O(n)      | O(n)    | O(n)       | O(n)  |
| Search            | O(1)\*    | O(n)    | O(n)       | O(n)  |
| Insert front      | O(1)      | O(1)    | O(1)       | O(n)  |
| Insert end        | O(1)      | O(1)    | O(1)       | O(n)  |
| Delete front      | O(1)      | O(1)    | O(1)       | O(n)  |
| Delete end        | O(1)      | O(1)    | O(1)       | O(n)  |
| Delete by pointer | O(1)      | O(1)    | O(1)       | O(n)  |

> \* If you already have a pointer to the node

---

## Pseudocode Example

### Node structure

```pseudo
class Node:
    data
    prev
    next

function insertFront(head, x):
    newNode = Node(x)
    newNode.next = head
    newNode.prev = null
    if head != null:
        head.prev = newNode
    head = newNode

function delete(node):
    if node.prev != null:
        node.prev.next = node.next
    if node.next != null:
        node.next.prev = node.prev
    delete node
```

# Key Characteristics
- Nodes have two pointers: prev and next
- Allows O(1) deletion of any node if pointer is known
- Easy traversal in both directions
- Requires more memory per node (two pointers)
- Slightly more complex logic than singly linked list

# Common Pitfalls
- Forgetting to update both next and prev pointers
- Not handling edge cases: head/tail deletions
- Memory leaks (forgetting to delete removed nodes)
- Dangling pointers (using a node after deletion)

# Use Cases
- Browser history (back/forward)
- Undo/Redo functionality
- LRU cache (Least Recently Used)
- Music/video playlists with next/previous
- Navigable linked data structures

# Related Structures
- [Arrays](01_Arrays.md) – good for random access but costly insertions/deletions
- [Singly Linked List](06_SinglyLinkedLists.md) – simpler, but only forward traversal
- [Circular Linked List](08_CircularLinkedLists.md) – tail connects back to head
