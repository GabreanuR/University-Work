# Bloom Filter

## Motivation

A **Bloom Filter** is a **probabilistic data structure** that efficiently tests whether an element **might be in a set** — with a chance of false positives, but **no false negatives**.

It’s useful when:
- You care about **speed** and **space efficiency**
- Occasional false positives are acceptable
- You need **fast membership tests** without storing all elements

---

## Key Characteristics

| Property            | Description                                      |
|---------------------|--------------------------------------------------|
| False Positives     | Yes – might say “in set” when it’s not           |
| False Negatives     | No – if it says “not in set”, it’s guaranteed    |
| Space Efficient     | Uses much less memory than hash sets             |
| Fast                | Insert and lookup in O(k) (constant-time)        |

---

## How It Works

1. Create a **bit array** of size `m`, initialized to 0
2. Choose `k` different **hash functions** `h1, h2, ..., hk`
3. To **insert(x)**:
    - Compute `h1(x), ..., hk(x)`
    - Set bits at all those positions to 1
4. To **check(x)**:
    - Compute `h1(x), ..., hk(x)`
    - If **any** bit is 0 → definitely not in set
    - If **all** bits are 1 → *possibly* in set

---

## Complexity

| Operation | Time     | Space        |
|-----------|----------|--------------|
| Insert    | O(k)     | O(m)         |
| Lookup    | O(k)     | O(m)         |

> Where `k` = number of hash functions, and `m` = size of bit array

---

## False Positive Probability

Let:
- `n` = number of inserted elements
- `m` = size of bit array
- `k` = number of hash functions

Then the false positive rate is approximately:

(1 - e^(-kn/m))^k

You can optimize k as:

k =(m/n)*ln(2)

# Pseudocode Example

```
initialize bit array of size m to 0
choose k independent hash functions h1...hk

function insert(x):
    for i from 1 to k:
        pos = hi(x) mod m
        bitarray[pos] = 1

function mightContain(x):
    for i from 1 to k:
        pos = hi(x) mod m
        if bitarray[pos] == 0:
            return false
    return true  // might be in set
```

# Common Pitfalls
- Bloom Filters cannot delete items
- False positives accumulate over time
- Cannot recover original inserted elements
- Require careful hash function design to avoid collisions

# Use Cases
- Databases: to check if value exists before disk lookup
- Web caching: test if URL is in cache
- Email spam filters
- Distributed systems (e.g., Cassandra, Bigtable)
- Compilers (checking reserved keywords fast)

# Related Structures
- [Skip Lists](09_SkipLists.md) – fast and probabilistic, but ordered
- [Hash Tables](10_HashTables.md) – accurate but memory-heavy
- [Trie](21_Tries.md) – prefix lookup structure, not probabilistic