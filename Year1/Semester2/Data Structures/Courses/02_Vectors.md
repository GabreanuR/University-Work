# Vectors (Dynamic Arrays)

## Motivation

Vectors are **dynamic arrays** that automatically resize when their capacity is exceeded. They combine the **fast access** of regular arrays with the **flexibility** of dynamic allocation.

Vectors are useful when:
- You don’t know the number of elements in advance
- You frequently add elements to the end
- You still want `O(1)` access by index

---

## Core Operations

| Operation        | Description                                  |
|------------------|----------------------------------------------|
| Access by index  | `v[i]`                                       |
| Update value     | `v[i] = x`                                   |
| Push back        | Add an element to the end (`v.push_back(x)`) |
| Pop back         | Remove the last element                      |
| Insert at index  | Insert at arbitrary position                 |
| Delete at index  | Remove element at specific index             |
| Resize           | Internal resizing of capacity                |

---

## Complexity Summary

| Operation       | Best Case | Average Case | Worst Case | Space Complexity |
|-----------------|-----------|--------------|-------------|-------------------|
| Access          | O(1)      | O(1)         | O(1)        | O(n)              |
| Update          | O(1)      | O(1)         | O(1)        | O(n)              |
| Push Back       | O(1)      | O(1)*        | O(n)**      | O(n)              |
| Pop Back        | O(1)      | O(1)         | O(1)        | O(n)              |
| Insert at index | O(n)      | O(n)         | O(n)        | O(n)              |
| Delete at index | O(n)      | O(n)         | O(n)        | O(n)              |

> **\*** Amortized constant time due to geometric resizing (e.g. 2x capacity)  
> **\*\*** Worst case occurs when reallocation and copying are triggered

---

## Key Characteristics

- **Dynamic resizing**: automatically allocates more memory when needed
- **Amortized constant time** for `push_back()`
- Internally maintains a **capacity** (allocated) and **size** (used)
- Stored in contiguous memory (like arrays)

---

## Pseudocode Examples

### Push Back (Simplified)

```pseudo
function push_back(vec, x):
    if vec.size == vec.capacity:
        resize(vec)
    vec[vec.size] = x
    vec.size += 1
