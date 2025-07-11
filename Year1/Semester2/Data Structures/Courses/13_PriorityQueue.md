# Priority Queue

## Motivation

A **priority queue** is an abstract data type similar to a regular queue or stack, but where each element has a **priority**, and elements are dequeued in **priority order** (not insertion order).

Use when:
- You want to always access the **highest (or lowest) priority element** quickly
- Order of insertion is not important, but priority is

---

## Behavior

- Elements are added with a **value** and a **priority**
- On removal, the **element with the highest priority** is returned first
- Priority can be **min-oriented** (lowest first) or **max-oriented** (highest first)

---

## Core Operations

| Operation      | Description                                |
|----------------|--------------------------------------------|
| insert(x, p)   | Add element `x` with priority `p`          |
| getTop()       | Return element with highest priority       |
| removeTop()    | Remove element with highest priority       |
| isEmpty()      | Check if the queue is empty                |
| size()         | Return the number of elements              |

---

## Common Implementations

| Method                       | Description                             | Time Complexity  |
|------------------------------|-----------------------------------------|------------------|
| Unsorted Array/Vec           | Insert: O(1), Remove: O(n)              | Poor performance |
| Sorted Array/Vec             | Insert: O(n), Remove: O(1)              | Not ideal        |
| Binary Heap (min/max)        | Balanced binary tree, usually via array | O(log n)         |
| Pairing Heap, Fibonacci Heap | More advanced, better amortized ops     | O(1)–O(log n)    |

**Binary Heap** is the most common and practical implementation.

---

## Complexity Summary (Binary Heap)

| Operation | Time     | Space |
|-----------|----------|-------|
| insert    | O(log n) | O(n)  |
| getTop    | O(1)     | O(n)  |
| removeTop | O(log n) | O(n)  |
| buildHeap | O(n)     | O(n)  |

---

## Pseudocode Example (Max Priority Queue – Binary Heap)

```pseudo
function insert(heap, value):
    add value at the end
    bubble up to restore heap property

function removeTop(heap):
    replace root with last element
    remove last element
    bubble down to restore heap property

function getTop(heap):
    return heap[0]
```

# Common Pitfalls
- Confusing max-heap with min-heap behavior
- Forgetting to restore heap property after insert/remove
- Assuming O(1) insertion/removal in all cases

# Use Cases
- Scheduling tasks by priority (OS, real-time systems)
- Dijkstra’s algorithm for shortest paths
- Huffman coding (data compression)
- A* pathfinding algorithm
- Event simulation systems
- Bandwidth/resource management

# Related Structures
- [Queues](04_Queues.md) – FIFO behavior, no priority
- [Heaps](12_Heaps.md) – commonly used to implement priority queues
- [Binary Search Tree](14_BST.md) – sorted access but slower top removal