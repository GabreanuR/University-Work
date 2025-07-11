# Queues (FIFO)

## Motivation

A **queue** is a linear data structure that follows the **First-In, First-Out (FIFO)** principle: the first element added is the first to be removed.

Queues are useful in:
- CPU/process scheduling
- Breadth-First Search (BFS)
- Data streams and buffering
- Simulations (e.g., waiting lines)

---

## Core Operations

| Operation   | Description                          |
|-------------|--------------------------------------|
| enqueue(x)  | Add element `x` to the rear          |
| dequeue()   | Remove the front element             |
| front()     | Access the front element             |
| rear()      | Access the rear element (optional)   |
| isEmpty()   | Check if the queue is empty          |
| size()      | Number of elements in the queue      |

---

## Complexity Summary (Array or Linked List)

| Operation   | Best Case | Average | Worst Case | Space  |
|-------------|-----------|---------|------------|--------|
| enqueue     | O(1)      | O(1)    | O(1)       | O(n)   |
| dequeue     | O(1)*     | O(1)    | O(1)       | O(n)   |
| front       | O(1)      | O(1)    | O(1)       | O(n)   |

> \* O(1) only when using a **circular array** or **linked list**.  
> Otherwise, `dequeue()` in a plain array may require shifting (`O(n)`).

---

## Pseudocode (Circular Array)

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
- Using arrays without wrap-around logic (circular buffer)
- Forgetting to resize when using dynamic arrays
- Confusing front and rear logic

# Use Cases
- CPU scheduling, I/O buffers
- Level-order traversal (BFS)
- Event-driven simulation
- Producer-consumer problems

# Related Structures
- [Vectors](02_Vectors.md) – Can be used to build a queue
- [Stacks](03_Stacks.md) – LIFO instead of FIFO
- [Deque](05_Deque.md) – Generalization of queues and stacks
- [Priority Queue](13_PriorityQueue.md) – Dequeues based on priority