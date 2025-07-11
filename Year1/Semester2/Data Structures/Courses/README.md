# Courses – Data Structures Theory

This section contains in-depth **theoretical explanations** of core data structures. Each topic includes:

- Motivation: Why this structure exists and where it's used
- Core operations and behaviors
- Time and space complexity analysis
- Pseudocode and sometimes real code snippets
- Comparisons with other structures

The goal is to provide a solid theoretical foundation that complements practical implementations from the [Labs](../Labs) section and exercises in the [Seminars](../Seminars) section.

---

## Available Topics

| #  | Data Structure                                     |
|----|----------------------------------------------------|
| 01 | [Arrays](01_Arrays.md)                             |
| 02 | [Vectors](02_Vectors.md)                           |
| 03 | [Stacks](03_Stacks.md)                             |
| 04 | [Queues](04_Queues.md)                             |
| 05 | [Deque](05_Deque.md)                               | 
| 06 | [Singly Linked Lists](06_SinglyLinkedLists.md)     |
| 07 | [Doubly Linked Lists](07_DoublyLinkedLists.md)     |
| 08 | [Circular Linked Lists](08_CircularLinkedLists.md) |
| 09 | [Skip Lists](09_SkipLists.md)                      |
| 10 | [Hash Tables](10_HashTables.md)                    |
| 11 | [Trees](11_Trees.md)                               |
| 12 | [Heaps](12_Heaps.md)                               |
| 13 | [Priority Queues](13_PriorityQueue.md)             |
| 14 | [Binary Search Trees](14_BST.md)                   |
| 15 | [AVL](15_AVL.md)                                   |
| 16 | [Splay Trees](16_Splay.md)                         |
| 17 | [Red-Black Trees](17_RedBlack.md)                  |
| 18 | [Sorting Algorithms](18_SortingAlgorithms.md)      |
| 19 | [B-Trees](19_BTrees.md)                            |
| 20 | [Bloom Filters](20_BloomFilters.md)                |
| 21 | [Tries](21_Tries.md)                               |
| 22 | [Graph Algorithms](22_Graphs.md)                   |
| 23 | [Computational Geometry](23_Geometry.md)           |

---

## Writing Conventions

Each file will generally follow this structure:

```markdown
# [Title]

## Motivation
Short description of the problem this structure solves.

## Core Operations
- insert()
- delete()
- search()
- ...

## Time Complexities
| Operation | Best | Average | Worst |
|-----------|------|---------|-------|
| Insert    | O(1) | O(1)    | O(n)  |
| ...

## Pseudocode
```pseudo
function insert(x):
    ...
