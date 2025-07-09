# Stacks (LIFO)

## Motivation

Stacks are linear data structures that follow the **Last-In, First-Out (LIFO)** principle.

They are useful when:
- You need to reverse a sequence
- You want to track history or backtrack
- You want to evaluate or parse expressions
- You're simulating function calls (call stack)

---

## Core Operations

| Operation   | Description                       |
|-------------|-----------------------------------|
| push(x)     | Add element `x` on top            |
| pop()       | Remove the top element            |
| top()       | Peek at the top element           |
| isEmpty()   | Check if the stack is empty       |
| size()      | Number of elements in the stack   |

---

## Complexity Summary

| Operation | Best Case | Average Case | Worst Case  | Space Complexity  |
|-----------|-----------|--------------|-------------|-------------------|
| push      | O(1)      | O(1)         | O(1)        | O(n)              |
| pop       | O(1)      | O(1)         | O(1)        | O(n)              |
| top       | O(1)      | O(1)         | O(1)        | O(n)              |
| isEmpty   | O(1)      | O(1)         | O(1)        | O(1)              |
| size      | O(1)      | O(1)         | O(1)        | O(1)              |

> All operations are constant time because stacks are typically implemented using arrays (vectors) or linked lists.

---

## Key Characteristics

- Follows **LIFO** (last in = first out)
- Typically implemented using:
  - Arrays / vectors (fixed or dynamic size)
  - Singly linked lists
- Only allows insertion/removal at one end ("the top")

---

## Pseudocode Examples

### Push and Pop (Array-based)

```pseudo
function push(stack, x):
    if stack.size == stack.capacity:
        resize(stack)
    stack[stack.size] = x
    stack.size += 1

function pop(stack):
    if stack.size == 0:
        error "Stack Underflow"
    stack.size -= 1
```

# Common Pitfalls
- Stack overflow if using fixed-size arrays and not resizing
- Stack underflow if calling pop() or top() on an empty stack
- Confusing "top" with index 0 (it's usually at the end in array-based stacks)

# Use Cases
- Function call stack (recursion)
- Syntax parsing (e.g., parentheses matching)
- Undo/Redo systems
- Depth-First Search (DFS)
- Expression evaluation (Postfix, Infix)

# Related Structures
- [Queues](./04_Queues.md) – FIFO instead of LIFO
- [Deques](./04_Queues.md) – Double-ended stack/queue hybrid
- [Vectors](./02_Vectors.md) – Can be used to implement stacks
