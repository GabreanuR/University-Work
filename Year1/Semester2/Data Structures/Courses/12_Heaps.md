# Heaps

## Motivation

A **heap** is a complete binary tree that satisfies the **heap property**:
- In a **min-heap**, every parent ≤ its children
- In a **max-heap**, every parent ≥ its children

Heaps are efficient when:
- You need to repeatedly access the **minimum or maximum** element
- You're implementing a **priority queue**
- You want an efficient, in-place **sorting algorithm** (HeapSort)

---

## Types of Heaps

| Type           | Description                                                 |
|----------------|-------------------------------------------------------------|
| Min-Heap       | Root is the minimum; each parent ≤ children                 |
| Max-Heap       | Root is the maximum; each parent ≥ children                 |
| Binary Heap    | Heap stored as array; complete binary tree                  |
| d-ary Heap     | Each node has d children (used in specialized cases)        |
| Fibonacci Heap | Advanced, better amortized bounds (rarely used in practice) |

---

## Core Operations

| Operation      | Description                                 |
|----------------|---------------------------------------------|
| insert(x)      | Add element and maintain heap structure     |
| extract_min()  | Remove the root (min/max)                   |
| get_min()      | Return the root element without removing it |
| heapify()      | Turn an array into a valid heap             |
| increase_key() | Increase priority of a node (in max-heap)   |
| decrease_key() | Decrease priority of a node (in min-heap)   |

---

## Complexity Summary

| Operation             | Best    | Average | Worst   | Space  |
|-----------------------|---------|---------|---------|--------|
| insert                | O(1)    | O(log n)| O(log n)| O(n)   |
| extract_min           | O(log n)| O(log n)| O(log n)| O(n)   |
| get_min               | O(1)    | O(1)    | O(1)    | O(n)   |
| heapify               | O(n)    | O(n)    | O(n)    | O(n)   |
| increase/decrease key | O(log n)| O(log n)| O(log n)| O(n)   |

---

## Heap as an Array

Given index `i`:
- Left child: `2i + 1`
- Right child: `2i + 2`
- Parent: `(i - 1) / 2`

---

## Pseudocode (Min-Heap Insert & Heapify)

### Insert

```pseudo
function insert(heap, x):
    heap.append(x)
    i = heap.size - 1
    while i > 0 and heap[parent(i)] > heap[i]:
        swap heap[i] with heap[parent(i)]
        i = parent(i)

function extract_min(heap):
    if heap is empty:
        error
    min = heap[0]
    heap[0] = heap[last]
    remove last
    heapify_down(heap, 0)
    return min

function heapify_down(heap, i):
    left = 2i + 1
    right = 2i + 2
    smallest = i
    if left < size and heap[left] < heap[smallest]:
        smallest = left
    if right < size and heap[right] < heap[smallest]:
        smallest = right
    if smallest ≠ i:
        swap heap[i], heap[smallest]
        heapify_down(heap, smallest)
```

# Common Pitfalls
- Mixing up min-heap and max-heap logic
- Off-by-one errors in array-based implementation
- Confusing heapify (build-heap) with heapify_down

# Use Cases
- Priority Queue (std::priority_queue)
- Dijkstra’s shortest path algorithm
- Huffman Coding (Greedy)
- Scheduling systems
- Real-time simulations (event queues)

# Related Structures
- [Binary Search Tree](./08_BST.md) – for ordered data with search
- [AVL Trees](./09_AVL.md) – better if you need fast search
- [Red-Black Trees](./11_RedBlack.md) – better if you need fast search
- [Hash Tables](./07_HashTables.md) – faster lookup, but no ordering
