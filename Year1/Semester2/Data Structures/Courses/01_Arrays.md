# Arrays

## Motivation

Arrays are one of the most fundamental data structures. They store a **fixed-size** collection of elements of the same type in **contiguous memory**.

They are used when:
- You know the number of elements in advance
- You need **constant-time access** to elements by index
- You want to work with simple, memory-efficient collections

---

## Core Operations

| Operation        | Description                            |
|------------------|----------------------------------------|
| Access by index  | `arr[i]`                               |
| Update value     | `arr[i] = x`                           |
| Traverse         | Iterate through all elements           |
| Search (unsorted)| Linear scan                            |
| Search (sorted)  | Binary search (if sorted)              |
| Insert/Delete    | Not supported efficiently              |

---

## Key Characteristics

- Fixed size (determined at allocation time)
- Stored in **contiguous memory**
- Supports **random access**
- Poor support for dynamic resizing or insertion/deletion

---

## Complexity Summary

| Operation     | Best Case | Average Case | Worst Case  | Space Complexity |
|---------------|-----------|--------------|-------------|-------------------|
| Access        | O(1)      | O(1)         | O(1)        | O(n)              |
| Update        | O(1)      | O(1)         | O(1)        | O(n)              |
| Linear Search | O(1)      | O(n)         | O(n)        | O(n)              |
| Binary Search | O(1)      | O(log n)     | O(log n)    | O(n)              |
| Insert (mid)  | O(n)      | O(n)         | O(n)        | O(n)              |
| Insert (end)  | O(1)      | O(1)         | O(1)        | O(n)              |
| Delete        | O(n)      | O(n)         | O(n)        | O(n)              |

---

## Pseudocode Examples

### Access and Update

```pseudo
function getElement(arr, index):
    return arr[index]

function setElement(arr, index, value):
    arr[index] = value

function search(arr, target):
    for i from 0 to length(arr) - 1:
        if arr[i] == target:
            return i
    return -1
```

## Common Pitfalls:
- Going out of bounds (arr[n] when n >= size)
- Forgetting that arrays have fixed size (use vectors if you need dynamic resizing)
- Mixing 0-based and 1-based indexing

## Use Cases:
- Static collections (like days of the week)
- Lookup tables (if you map keys to indexes)
- Base for more advanced structures (e.g., Heaps, Hash Tables)

## Related Structures
- [Vectors](./02_Vectors.md) – dynamic version of arrays
- [Linked Lists](./05_LinkedLists.md) – dynamic size with slower access
