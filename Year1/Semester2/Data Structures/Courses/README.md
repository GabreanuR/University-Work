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

| #   | Data Structure               | Link                                 |
|-----|------------------------------|--------------------------------------|
| 01  | Arrays                       | [Arrays.md](./01_Arrays.md)          |
| 02  | Vectors                      | [Vectors.md](./02_Vectors.md)        |
| 03  | Stacks                       | [Stacks.md](./03_Stacks.md)          |
| 04  | Queues                       | [Queues.md](./04_Queues.md)          |
| 05  | Linked Lists                 | [LinkedLists.md](./05_LinkedLists.md)|
| 06  | Skip Lists                   | [SkipLists.md](./06_SkipLists.md)    |
| 07  | Hash Tables                  | [HashTables.md](./07_HashTables.md)  |
| 08  | Binary Search Trees (BST)    | [BST.md](./08_BST.md)                |
| 09  | AVL Trees                    | [AVL.md](./09_AVL.md)                |
| 10  | Splay Trees                  | [Splay.md](./10_Splay.md)            |
| 11  | Red-Black Trees              | [RedBlack.md](./11_RedBlack.md)      |
| 12  | Heaps (Min, Max, Binary)     | [Heaps.md](./12_Heaps.md)            |
| 13  | B-Trees                      | [BTrees.md](./13_BTrees.md)          |
| 14  | Sorting Algorithms           | [Sorting.md](./14_Sorting.md)        |
| 15  | Graph Algorithms (MST etc.)  | [Graphs.md](./15_Graphs.md)          |
| 16  | Computational Geometry       | [Geometry.md](./16_Geometry.md)      |

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
