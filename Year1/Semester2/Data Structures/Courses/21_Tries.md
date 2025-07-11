# Trie (Prefix Tree)

## Motivation

A **Trie** (a.k.a. prefix tree) is a tree-like data structure used for storing strings where:
- Nodes represent **prefixes**
- Paths from root to leaves represent **entire keys**

It is extremely useful when:
- You work with **many strings** (e.g., dictionary, autocomplete)
- You want **fast prefix queries**
- You need **space-efficient string search**

---

## Key Characteristics

- Each edge represents a character
- Each node represents a prefix
- Root is an empty prefix
- Leaves usually mark **end of word**
- Fast insertion and lookup — independent of alphabet size

---

## Complexity

Let:
- `n` = number of words
- `L` = average length of word
- `Σ` = size of alphabet (e.g. 26 for lowercase letters)

| Operation     | Time | Space    |
|---------------|------|----------|
| Insert word   | O(L) | O(n × Σ) |
| Search word   | O(L) | O(n × Σ) |
| Search prefix | O(L) | O(n × Σ) |

---

## Node Structure

Each node typically contains:
- A map/array of children (char → TrieNode)
- A boolean `isEnd` to mark the end of a word

---

## Pseudocode

```pseudo
class TrieNode:
    children = map/array of characters → TrieNode
    isEnd = false

class Trie:
    root = TrieNode()

function insert(word):
    node = root
    for char in word:
        if char not in node.children:
            node.children[char] = new TrieNode()
        node = node.children[char]
    node.isEnd = true

function search(word):
    node = root
    for char in word:
        if char not in node.children:
            return false
        node = node.children[char]
    return node.isEnd

function startsWith(prefix):
    node = root
    for char in prefix:
        if char not in node.children:
            return false
        node = node.children[char]
    return true
```

# Advantages
- Faster than hash maps for prefix or sorted queries
- Can list all strings with a given prefix efficiently
- Memory sharing through common prefixes

# Limitations
- Can use more memory than hashing (lots of pointers)
- Not good for small datasets
- Harder to implement than plain maps

# Use Cases
- Autocomplete systems
- Spell checking / correction
- IP routing (longest prefix match)
- Word games (e.g., Boggle, Scrabble)
- Suffix trie for substring search (advanced)

# Related Structures
- [Hash Tables](10_HashTables.md) – fast for exact match, not prefix
- [AVL Trees](15_AVL.md) – ordered structure, but not optimized for strings
- [Bloom Filters](20_BloomFilters.md) – space efficient but probabilistic