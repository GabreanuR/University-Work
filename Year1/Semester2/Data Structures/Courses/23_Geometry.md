# Computational Geometry

## Motivation

Computational geometry studies **algorithms for geometric problems**. It is used in:

- Computer graphics and games
- GIS (Geographic Information Systems)
- Robotics and computer vision
- Collision detection
- Geometry-based competitive programming

---

## Fundamental Concepts

### Points and Vectors

A point `P(x, y)` is also a vector from the origin.  
A segment is defined by two points: `A(x1, y1)`, `B(x2, y2)`.

### Vector Operations

- **Dot Product**: `A ⋅ B = Ax * Bx + Ay * By`  
  → Angle between vectors
- **Cross Product** (2D): `A × B = Ax * By - Ay * Bx`  
  → Orientation and area

---

### Orientation Test

Given 3 points `A`, `B`, `C`:

- Compute vector AB and AC
- Then cross product: `AB × AC`

| Result | Interpretation  |
|--------|-----------------|
| < 0    | Right turn (CW) |
| > 0    | Left turn (CCW) |
| = 0    | Collinear       |

### Pseudocode Example

```
function orientation(A, B, C):
    val = (B.x - A.x) * (C.y - A.y) - (B.y - A.y) * (C.x - A.x)
    if val > 0: return "left"
    if val < 0: return "right"
    return "collinear"
```

# Segment Intersection
Two segments AB and CD intersect if:
- Orientation tests give opposite results:
  - orient(A,B,C) != orient(A,B,D)
  - orient(C,D,A) != orient(C,D,B)
- Plus special checks if points are collinear and overlapping

```
function doIntersect(A, B, C, D):
    o1 = orientation(A, B, C)
    o2 = orientation(A, B, D)
    o3 = orientation(C, D, A)
    o4 = orientation(C, D, B)

    if o1 != o2 and o3 != o4:
        return true

    // Special case: collinear + onSegment
    if o1 == 0 and onSegment(A, C, B): return true
    if o2 == 0 and onSegment(A, D, B): return true
    if o3 == 0 and onSegment(C, A, D): return true
    if o4 == 0 and onSegment(C, B, D): return true

    return false

function onSegment(P, Q, R):
    return min(P.x, R.x) ≤ Q.x ≤ max(P.x, R.x) and
           min(P.y, R.y) ≤ Q.y ≤ max(P.y, R.y)
```

- Time: O(1) per pair
- Use: collision detection, line intersection, polygon tests

# Convex Hull (Graham Scan)

Find the smallest convex polygon enclosing a set of points.

```
function convexHull(points):
    sort points by x (and y if tie)
    lower = empty stack
    for p in points:
        while size(lower) ≥ 2 and orientation(lower[-2], lower[-1], p) ≠ "left":
            lower.pop()
        lower.push(p)

    upper = empty stack
    for p in reversed(points):
        while size(upper) ≥ 2 and orientation(upper[-2], upper[-1], p) ≠ "left":
            upper.pop()
        upper.push(p)

    remove last point of upper and lower (duplicate)
    return lower + upper
```

- Time: O(n log n)
- Use: minimal area enclosing shape, visibility polygons, collision boundaries

# Other Common Problems

| Problem                         | Idea                   | Time       |
|---------------------------------|------------------------|------------|
| Point in polygon                | Ray casting or winding | O(n)       |
| Closest pair of points          | Divide & conquer       | O(n log n) |
| Polygon area (Shoelace formula) | Cross product sum      | O(n)       |
| Circle intersection             | Algebraic equations    | O(1)       |

# Common Pitfalls
- Confusing cross vs dot product
- Floating-point errors → prefer integer geometry if possible
- Collinearity edge cases
- Forgetting to sort points by angle or coordinate

# Use Cases
- Hitbox detection in games
- Robot navigation and obstacle avoidance
- Shape matching / pattern recognition
- Geometry-based AI pathfinding

# Related Topics
- [Binary Search](14_BST.md) – sometimes used on angles or distances
- [Graphs](22_Graphs.md) – many geometry problems reduce to graphs