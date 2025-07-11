# Deque (Double-Ended Queues)

## Motivation

A **deque** (double-ended queue) is a generalization of both **queues** and **stacks**:
- Elements can be inserted and removed from **both ends**
- Can behave like:
    - A queue (FIFO)
    - A stack (LIFO)
    - Or a combination of both

---

## Core Operations

| Operation       | Description                                  |
|-----------------|----------------------------------------------|
| push_front(x)   | Insert `x` at the front                      |
| push_back(x)    | Insert `x` at the back                       |
| pop_front()     | Remove and return front element              |
| pop_back()      | Remove and return rear element               |
| front()         | Peek front element without removing          |
| back()          | Peek back element without removing           |
| isEmpty()       | Check if the deque is empty                  |
| size()          | Get the number of elements                   |

---

## Complexity Summary

### With Doubly Linked List (recommended)

| Operation     | Best | Average | Worst | Space  |
|---------------|------|---------|-------|--------|
| push_front    | O(1) | O(1)    | O(1)  | O(n)   |
| push_back     | O(1) | O(1)    | O(1)  | O(n)   |
| pop_front     | O(1) | O(1)    | O(1)  | O(n)   |
| pop_back      | O(1) | O(1)    | O(1)  | O(n)   |

### With Array (like `std::deque`)

| Operation     | Best | Average | Worst (realloc/shift)   | Space  |
|---------------|------|---------|-------------------------|--------|
| push_front    | O(1) | O(1)    | O(n)                    | O(n)   |
| push_back     | O(1) | O(1)    | O(n)                    | O(n)   |
| pop_front     | O(1) | O(1)    | O(n)                    | O(n)   |
| pop_back      | O(1) | O(1)    | O(n)                    | O(n)   |

> Array-based deque are faster in practice due to contiguous memory, but worst-case O(n) when shifting/resizing is required.

---

## Pseudocode (Linked List Implementation)

```pseudo
class DequeNode:
    value
    prev
    next

class Deque:
    front
    back
    size

function push_front(x):
    newNode = DequeNode(x)
    newNode.next = front
    if front != null:
        front.prev = newNode
    front = newNode
    if back == null:
        back = newNode
    size += 1

function pop_back():
    if back == null:
        error "Empty Deque"
    value = back.value
    back = back.prev
    if back != null:
        back.next = null
    else:
        front = null
    size -= 1
    return value
```

# Common Pitfalls
- Confusing front/rear logic when indexing
- Using array-based implementation without capacity handling
- Assuming constant-time on both ends without checking implementation details

# Use Cases
- Sliding window algorithms (e.g., max/min in a range)
- Palindrome checking
- Undo/Redo functionality
- BFS with level markers
- Task schedulers (double-ended priority)

# Related Structures
- [Vectors](02_Vectors.md) – Can simulate deque with cost
- [Stacks](03_Stacks.md) – LIFO only
- [Queues](04_Queues.md) – FIFO only
- [Priority Queue](13_PriorityQueue.md) – For priority-based removal