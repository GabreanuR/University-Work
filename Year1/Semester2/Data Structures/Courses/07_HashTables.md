# Hash Tables

## Motivation

A **hash table** is a data structure that provides **fast key-based access** to values using a **hash function**.

It is ideal when:
- You want to store key-value pairs
- You need **average-case O(1)** lookups, insertions, deletions
- Order of elements doesn’t matter

---

## Core Concepts

| Concept             | Description                                        |
|---------------------|----------------------------------------------------|
| Key                 | Identifier for data (e.g. string, int)             |
| Hash Function       | Maps key → integer index                           |
| Hash Table (array)  | Stores values at computed indices                  |
| Collision           | Two keys map to the same index                     |

---

## Core Operations

| Operation     | Description                             |
|---------------|-----------------------------------------|
| insert(k, v)  | Add value `v` with key `k`              |
| get(k)        | Retrieve value by key `k`               |
| delete(k)     | Remove key-value pair                   |
| contains(k)   | Check if key `k` exists                 |

---

## Complexity Summary

| Operation | Best | Average | Worst | Space  |
|-----------|------|---------|-------|--------|
| insert    | O(1) | O(1)    | O(n)  | O(n)   |
| search    | O(1) | O(1)    | O(n)  | O(n)   |
| delete    | O(1) | O(1)    | O(n)  | O(n)   |

> Worst case occurs when all keys collide and degrade to a list.  
> Good hash functions and resizing keep performance close to O(1).

---

## Collision Resolution Techniques

| Technique         | Description                                         |
|-------------------|-----------------------------------------------------|
| Chaining          | Store multiple elements in a list at the same index |
| Open Addressing   | Find another slot (e.g., linear probing)            |
| Linear Probing    | Try next index (i+1, i+2...)                        |
| Quadratic Probing | Try i + 1², i + 2², etc.                            |
| Double Hashing    | Use a second hash function                          |

---

## Pseudocode (Chaining)

```pseudo
function insert(table, key, value):
    index = hash(key) mod table.size
    if table[index] is empty:
        table[index] = new list
    for (k, v) in table[index]:
        if k == key:
            v = value
            return
    table[index].append((key, value))

function get(table, key):
    index = hash(key) mod table.size
    for (k, v) in table[index]:
        if k == key:
            return v
    return null
```

# Common Pitfalls
- Using poor hash functions (e.g. just length(key))
- Not resizing when load factor grows (common threshold: 0.75)
- Forgetting to handle duplicate keys properly
- Ignoring worst-case scenarios (like DoS attacks via hash collisions)

#Use Cases
- Dictionaries (string → value)
- Symbol tables in compilers
- Caching and memoization
- Counting frequency of elements
- Lookup tables (e.g., phone book, DNS)

## Hash Sets / Unordered Sets

A **hash set** is a simplified version of a hash table that stores only **keys**, not key-value pairs.

In C++:  
- `std::unordered_set<T>` is built on top of a hash table  
- Internally uses hashing + collision resolution  
- Offers average O(1) insert, delete, search

Common operations:
- `insert(x)` – Add element `x`
- `contains(x)` – Check if `x` exists
- `erase(x)` – Remove `x` if present

# Related Structures
- [Arrays](./01_Arrays.md) – good for index-based access, no keys
- [Binary Search Trees](./08_BST.md) – better when data must be sorted
- [Bloom Filters](./17_BloomFilters.md) – space-efficient approximate sets
