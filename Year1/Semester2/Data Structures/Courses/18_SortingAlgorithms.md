# Sorting Algorithms

## Motivation

**Sorting** is a core algorithmic problem used in:
- Organizing data for efficient access (binary search, grouping, deduplication)
- Solving real-world tasks (ranking, scheduling, clustering)
- Foundation for more complex algorithms (e.g. in graphs or geometry)

---

## Classification

| Criteria         | Categories                              |
|------------------|-----------------------------------------|
| Time Complexity  | O(n²), O(n log n), O(n) (special cases) |
| Comparison-based | Yes: QuickSort, MergeSort, HeapSort     |
|                  | No: Counting, Radix, Bucket             |
| Stable Sorting   | Yes: Merge, Insertion, Bubble, Counting |
| In-place         | Yes: Quick, Heap, Bubble, Insertion     |
| Adaptive         | Yes: Insertion, Bubble                  |

---

## Complexity Summary

| Algorithm      | Best       | Avg        | Worst      | Space    | Stable |
|----------------|------------|------------|------------|----------|--------|
| Bubble Sort    | O(n)       | O(n²)      | O(n²)      | O(1)     | Yes    |
| Insertion Sort | O(n)       | O(n²)      | O(n²)      | O(1)     | Yes    |
| Selection Sort | O(n²)      | O(n²)      | O(n²)      | O(1)     | No     |
| Merge Sort     | O(n log n) | O(n log n) | O(n log n) | O(n)     | Yes    |
| Quick Sort     | O(n log n) | O(n log n) | O(n²)      | O(log n) | No     |
| Heap Sort      | O(n log n) | O(n log n) | O(n log n) | O(1)     | No     |
| Count Sort     | O(n + k)   | O(n + k)   | O(n + k)   | O(k)     | Yes    |
| Radix Sort     | O(nk)      | O(nk)      | O(nk)      | O(n + k) | Yes    |

> `k` is the range of values or number of digits

---

## Pseudocode – Core Algorithms

### Bubble Sort (Simple but slow)

```pseudo
function bubbleSort(A):
    for i from 0 to n-1:
        for j from 0 to n-2-i:
            if A[j] > A[j+1]:
                swap A[j], A[j+1]
```

### Insertion Sort (Great for small/mostly sorted arrays)

```
function insertionSort(A):
    for i from 1 to n-1:
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
```

### Selection Sort

```
function selectionSort(A):
    n = length(A)
    for i from 0 to n - 2:
        minIndex = i
        for j from i+1 to n - 1:
            if A[j] < A[minIndex]:
                minIndex = j
        swap A[i], A[minIndex]
```

### Merge Sort (Stable, recursive, O(n log n))

```
function mergeSort(A):
    if length(A) ≤ 1:
        return A
    mid = n / 2
    left = mergeSort(A[0..mid-1])
    right = mergeSort(A[mid..n-1])
    return merge(left, right)

function merge(L, R):
    result = []
    while L and R:
        if L[0] ≤ R[0]:
            result.append(L.pop_front())
        else:
            result.append(R.pop_front())
    return result + L + R
```

### Quick Sort (Fast but unstable, worst case O(n²))

```
function quickSort(A, low, high):
    if low < high:
        pi = partition(A, low, high)
        quickSort(A, low, pi - 1)
        quickSort(A, pi + 1, high)

function partition(A, low, high):
    pivot = A[high]
    i = low - 1
    for j from low to high - 1:
        if A[j] < pivot:
            i += 1
            swap A[i], A[j]
    swap A[i + 1], A[high]
    return i + 1
```

### Heap Sort (In-place, not stable)

```
function heapSort(A):
    buildMaxHeap(A)
    for i from n-1 downto 1:
        swap A[0], A[i]
        heapify(A, 0, i)

function buildMaxHeap(A):
    for i from floor(n/2) downto 0:
        heapify(A, i, n)

function heapify(A, i, n):
    largest = i
    l = 2*i + 1
    r = 2*i + 2
    if l < n and A[l] > A[largest]:
        largest = l
    if r < n and A[r] > A[largest]:
        largest = r
    if largest ≠ i:
        swap A[i], A[largest]
        heapify(A, largest, n)
```

### Count Sort (Non-comparison, integers only)

```
function countSort(A, k):
    count = array of size k initialized with 0
    for x in A:
        count[x] += 1
    index = 0
    for i from 0 to k-1:
        while count[i] > 0:
            A[index] = i
            index += 1
            count[i] -= 1
```

### Radix Sort

```
function radixSort(A, d):
    for i from 1 to d:
        A = stableCountingSort(A, i-th digit)

function stableCountingSort(A, digitPosition):
    count = array of size 10 initialized with 0
    output = array of same size as A

    for x in A:
        digit = extractDigit(x, digitPosition)
        count[digit] += 1

    for i from 1 to 9:
        count[i] += count[i - 1]

    for i from length(A) - 1 downto 0:
        digit = extractDigit(A[i], digitPosition)
        output[count[digit] - 1] = A[i]
        count[digit] -= 1

    return output
```

## When to Use What

| Situation                                                 | Recommended Algorithm       |
|-----------------------------------------------------------|-----------------------------|
| Small or nearly sorted array                              | Insertion Sort              |
| Simple to understand / teach                              | Bubble Sort, Selection Sort |
| Guaranteed O(n log n) + Stable                            | Merge Sort                  |
| Average case fast + In-place                              | Quick Sort                  |
| Worst-case O(n log n) + In-place                          | Heap Sort                   |
| Integers in small range (e.g. \[0, 100])                  | Counting Sort               |
| Large integers with fixed digit count (e.g. 6-digit ZIPs) | Radix Sort                  |
| Memory is a concern                                       | In-place sorts: Quick, Heap |
| Need sort + map structure                                 | Use `std::map` / RB-Tree    |


# Related Topics
- [Hash Tables](10_HashTables.md) – not sorting but fast lookup
- [Heap](12_Heaps.md) – used in HeapSort
- [Graph Algorithms](22_Graphs.md) – many depend on sorted edges (e.g., Kruskal)