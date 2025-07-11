# Graphs

## Motivation

Graphs are a fundamental structure for modeling **relationships** between entities. Nodes (vertices) represent entities, and edges represent connections.

---

## Types of Graphs

| Type                     | Description                          |
|--------------------------|--------------------------------------|
| Directed (digraph)       | Edges have direction (A → B)         |
| Undirected               | Edges are bidirectional (A — B)      |
| Weighted                 | Each edge has a cost or weight       |
| Unweighted               | Edges have no cost (assumed 1)       |
| Cyclic / Acyclic         | Contains / does not contain cycles   |
| Connected / Disconnected | One or multiple connected components |
| DAG                      | Directed Acyclic Graph               |

---

## Graph Representations

### 1. Adjacency Matrix

- 2D matrix `adj[n][n]`
- `adj[i][j] = 1` if edge from i to j exists

Pros: Easy to implement, constant-time edge check  
Cons: High space: O(n²)

### 2. Adjacency List

- Array of lists: `adj[i] = list of neighbors of i`
- Good for sparse graphs

Pros: Space efficient (O(n + m))  
Cons: Slower edge checks

---

## Core Algorithms

### Breadth-First Search (BFS)

- Explores level-by-level from a start node
- Good for shortest path in unweighted graphs

```pseudo
function BFS(graph, start):
    visited = set()
    queue = new queue()
    queue.enqueue(start)
    visited.add(start)

    while queue not empty:
        node = queue.dequeue()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.enqueue(neighbor)
```
Time: O(n + m)

Use case: Shortest path (unweighted), connected components, bipartite check

### Depth-First Search (DFS)

- Explores deep before wide
- Useful for cycle detection, topological sort, components

```
function DFS(node):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            DFS(neighbor)
```

Time: O(n + m)

### Topological Sort (for DAGs)

- Order of tasks with dependencies

```
function topoSort(graph):
    visited = set()
    stack = []

    for node in graph:
        if node not in visited:
            dfsTopo(node, visited, stack)

    return reverse(stack)

function dfsTopo(node, visited, stack):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfsTopo(neighbor, visited, stack)
    stack.append(node)
```

# Minimum Spanning Tree (MST)

## Kruskal's Algorithm
- Greedy on edges sorted by weight
- Uses Disjoint Set (Union-Find)
- Time: O(m log m)
- Space: O(n)

## Prim's Algorithm
- Greedy from one vertex, use a priority queue (heap)
- Time: O(m log n)
- Space: O(n)

# Shortest Paths

## Dijkstra’s Algorithm
- Finds shortest path from one node to all others
- Works only with non-negative weights

```
function dijkstra(graph, source):
    dist = map with ∞, dist[source] = 0
    priorityQueue = (source, 0)

    while priorityQueue not empty:
        u = node with smallest distance
        for each neighbor v of u:
            if dist[u] + weight(u, v) < dist[v]:
                dist[v] = dist[u] + weight(u, v)
```

Time: O(m log n) with heap

## Bellman-Ford
- Handles negative weights
- Can detect negative cycles
- Time: O(n × m)

## Floyd-Warshall (All-Pairs)
- Dynamic programming
- Works on dense graphs
- Time: O(n³)

# Summary Table

| Algorithm      | Use Case                        | Time Complexity |
|----------------|---------------------------------|-----------------|
| BFS            | Unweighted shortest path        | O(n + m)        |
| DFS            | Connected components, cycles    | O(n + m)        |
| Topo Sort      | DAG ordering                    | O(n + m)        |
| Kruskal        | Minimum Spanning Tree           | O(m log m)      |
| Prim           | Minimum Spanning Tree           | O(m log n)      |
| Dijkstra       | Shortest path (non-neg weights) | O(m log n)      |
| Bellman-Ford   | Negative weights, cycle check   | O(n × m)        |
| Floyd-Warshall | All pairs shortest paths        | O(n³)           |

# Common Pitfalls
- Not checking for visited nodes in DFS/BFS → infinite loops
- Using Dijkstra with negative weights → incorrect results
- Modifying graph during iteration
- Forgetting disconnected components

# Use Cases
- Social networks (friend suggestions, community detection)
- Maps & GPS (routing)
- Network reliability
- Scheduling with constraints (topo sort)
- Game AI (pathfinding)

# Related Structures
- [Stacks](03_Stacks.md) – used in DFS and Topo Sort
- [Queues](04_Queues.md) – used in BFS
- [Heaps](12_Heaps.md) – used in Prim and Dijkstra