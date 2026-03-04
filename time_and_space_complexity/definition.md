# Time and Space Complexity (Beginner Notes)

## Time Complexity
Time complexity means: if input size grows, how many more steps the code takes.

- It is about growth of steps, not exact seconds.
- More input -> usually more steps.

Simple metaphor:
- Finding one photo in your phone gallery.
- More photos -> more time to find one photo.

### Common time complexities

`O(1)` (constant)
- Work stays almost same even if input grows.
- Example: `arr[5]` (array index access).

`O(log n)` (logarithmic)
- Input gets cut in half each step.
- Example: binary search on a sorted array.

`O(n)` (linear)
- Work grows with input size.
- Example: checking each number once to find a target.

`O(n log n)` (linearithmic)
- Slightly more than linear, much better than quadratic.
- Example: merge sort, heap sort, quick sort (average case).

`O(n^2)` (quadratic)
- Work grows very fast (usually nested loops).
- Example: compare every item with every other item.

`O(2^n)` (exponential)
- Growth explodes for larger `n`.
- Example: brute force include/exclude recursion over all subsets.

`O(n!)` (factorial)
- Even worse growth than exponential.
- Example: brute force all permutations.

Simple metaphor for `O(n^2)`:
- In a class, each student shakes hands with every other student.

## Space Complexity
Space complexity means: how much extra memory (RAM) the algorithm uses as input grows.

- We count extra memory used by the algorithm.
- Input itself is usually not counted as extra space.

Simple metaphor:
- Your phone RAM while apps are running.
- More running apps/data -> more RAM needed.

### Common space complexities

`O(1)` extra space
- Uses fixed extra variables only.
- Example:
  - `total = 0`
  - loop through array and keep adding to `total`

`O(n)` extra space
- Extra memory grows with input size.
- Example:
  - create new list and copy/transform each element from original list


## Why this matters in real world
- RAM is limited (on device and servers).
- More memory usage can slow systems and increase cloud cost.
- Better space-efficient code helps scale to more users.
