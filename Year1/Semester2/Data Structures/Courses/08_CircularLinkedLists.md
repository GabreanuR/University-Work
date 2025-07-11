# Circular Linked Lists (CLL)

## Motivation

A **circular linked list** is a variant of a linked list in which:
- The **last node points back to the first node** instead of `null`
- It forms a **circular structure** with no clear beginning or end

There are two main types:
- **Singly Circular Linked List**: each node has one pointer (`next`)
- **Doubly Circular Linked List**: each node has two pointers (`next`, `prev`), and both ends are connected

Useful when:
- You want to **loop through data continuously**
- No clear head/tail separation is needed
- You want constant-time rotation or cycling

---

# Core Operations (Singly Circular)

| Operation      | Description                             |
|----------------|-----------------------------------------|
| insertFront(x) | Add node at the beginning               |
| insertEnd(x)   | Add node at the end                     |
| delete(x)      | Remove node with value `x`              |
| traverse()     | Print all elements (stop at head again) |

# Complexity Summary

| Operation    | Best | Average | Worst | Space |
|--------------|------|---------|-------|-------|
| Insert front | O(1) | O(1)    | O(1)  | O(n)  |
| Insert end   | O(n) | O(n)    | O(n)  | O(n)  |
| Delete       | O(n) | O(n)    | O(n)  | O(n)  |
| Traverse     | O(n) | O(n)    | O(n)  | O(n)  |

> You can make insertEnd() O(1) if you maintain a tail pointer.

## Node Structure (Singly Circular)

```pseudo
class Node:
    data
    next

function insertEnd(head, x):
    newNode = Node(x)
    if head == null:
        newNode.next = newNode
        head = newNode
        return
    curr = head
    while curr.next != head:
        curr = curr.next
    curr.next = newNode
    newNode.next = head
```

# Common Pitfalls
- Infinite loops if you don’t stop at the head during traversal
- Forgetting to reset links correctly when deleting
- Edge case: inserting or deleting the only node
- Mistakenly treating it like a linear list

# Special Features of Circular Lists
- Can loop indefinitely through nodes
- Natural for round-robin scheduling, games, buffering
- Head and tail are logically equal (depends on context)

# Use Cases
- Round-robin CPU/task scheduling
- Multiplayer games (loop through players)
- Circular buffers in streaming or audio processing
- Musical chairs / Josephus problem

# Related Structures
- [Singly Linked List](06_SinglyLinkedLists.md) – standard linear structure
- [Doubly Linked List](07_DoublyLinkedLists.md) – bidirectional
- [Queues](04_Queues.md) – often implemented using circular buffers