# Queues and Deques

## Motivation

A **queue** is a linear data structure that follows the **First-In, First-Out (FIFO)** principle: the first element added is the first to be removed.

Queues are used in:
- Scheduling (CPU, printers, processes)
- Breadth-First Search (BFS)
- Data streams and buffering

A **deque** (double-ended queue) generalizes queues and stacks:
- Supports insertion/removal at both ends
- Can behave like a queue, stack, or both

---

## Queue Operations (FIFO)

| Operation   | Description                          |
|-------------|--------------------------------------|
| enqueue(x)  | Add element `x` to the rear          |
| dequeue()   | Remove the front element             |
| front()     | Access the front element             |
| rear()      | Access the last element (optional)   |
| isEmpty()   | Check if the queue is empty          |
| size()      | Number of elements in the queue      |

---

## Deque Operations (Double-Ended)

| Operation         | Description                                   |
|-------------------|-----------------------------------------------|
| push_front(x)     | Insert at the front                           |
| push_back(x)      | Insert at the back                            |
| pop_front()       | Remove from front                             |
| pop_back()        | Remove from back                              |
| front(), back()   | Peek at front or back                         |
| isEmpty(), size() | Same as in queue                              |

---

## Complexity Summary

### Queue (Array or Linked List)

| Operation   | Best Case | Average | Worst Case | Space  |
|-------------|-----------|---------|------------|--------|
| enqueue     | O(1)      | O(1)    | O(1)       | O(n)   |
| dequeue     | O(1)*     | O(1)    | O(1)       | O(n)   |
| front       | O(1)      | O(1)    | O(1)       | O(n)   |

> *: `dequeue()` is O(1) only if implemented using circular buffer or linked list. Otherwise shifting can cause O(n).

### Deque (with array or doubly linked list)

| Operation      | Best | Average | Worst | Space  |
|----------------|------|---------|-------|--------|
| push_front     | O(1) | O(1)    | O(n)  | O(n)   |
| push_back      | O(1) | O(1)    | O(n)  | O(n)   |
| pop_front      | O(1) | O(1)    | O(n)  | O(n)   |
| pop_back       | O(1) | O(1)    | O(n)  | O(n)   |

> O(n) happens in array-based deques when resizing or shifting is needed.

---

## Pseudocode (Queue – Circular Array)

```pseudo
initialize queue with capacity
front ← 0
rear ← -1
size ← 0

function enqueue(x):
    if size == capacity:
        error "Queue Overflow"
    rear = (rear + 1) mod capacity
    queue[rear] = x
    size += 1

function dequeue():
    if size == 0:
        error "Queue Underflow"
    front = (front + 1) mod capacity
    size -= 1

function front():
    return queue[front]
```

# Common Pitfalls
- Using arrays without wrap-around logic (circular queue)
- Forgetting to resize when using dynamic arrays
- Confusing front and rear logic
- For deque, assuming constant time at both ends in all implementations (not true for array-based)

# Use Cases
## Queues:
- CPU scheduling, IO buffers
- Level-order traversal (BFS in trees/graphs)
- Simulation (e.g., waiting lines)

## Deques:
- Sliding window problems (e.g., max/min in range)
- Palindrome checking
- Undo/Redo buffers
- Stack + Queue hybrid behaviors

# Related Structures
- [Stacks](./03_Stacks.md) – LIFO instead of FIFO
- [Vectors](./02_Vectors.md) – Can be used to build a queue or deque
- [Priority Queue](./12_Heaps.md) – Elements dequeued by priority
