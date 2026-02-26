# How to declare array
arr = [1, 2, 3, 4, 5, 6]
empty_array = []
print([0] * 5)  # [0, 0, 0, 0, 0] | O(n) -> creates n elements

# Accessing value
print(arr[1])  # 2 | O(1) -> direct index access

# Looping through array
for num in arr:
    print(num)  # 1 2 3 4 5 6 (one per line) | O(n) total
for i in range(len(arr)):
    print(arr[i])  # 1 2 3 4 5 6 (one per line) | O(n) total

# Inserting in array
arr.append(7)
print(arr)  # [1, 2, 3, 4, 5, 6, 7] | O(1) amortized -> append at end

# Updating array
# arr[0] = 10          # O(1) -> update by index
# arr.insert(2, 20)    # O(n) -> shift elements to right
# arr.pop()            # O(1) -> remove last element
# arr.pop(2)           # O(n) -> shift elements to left
# arr.remove(10)       # O(n) -> search + shift

# Searching in array
print("Is 3 in array", 3 in arr)  # Is 3 in array True | O(n) -> linear search
print(arr)  # [1, 2, 3, 4, 5, 6, 7]
print("Returns index of value 4", arr.index(4))  # Returns index of value 4 3 | O(n) -> linear search
print(arr)  # [1, 2, 3, 4, 5, 6, 7]

# Slicing the array
# All slicing operations return a new array (extra space)
# syntax: arr[start: end: step]
print(arr[1:4])  # [2, 3, 4] | O(k) time, O(k) space
print(arr[:3])  # [1, 2, 3] | O(k) time, O(k) space
print(arr[::-1])  # [7, 6, 5, 4, 3, 2, 1] | O(n) time, O(n) space -> reversed copy
print(arr[-4:-1])  # [4, 5, 6] | O(k) time, O(k) space

# Built-in methods
print(len(arr))  # 7 | O(1)
print(sum(arr))  # 28 | O(n)
print(max(arr))  # 7 | O(n)
print(min(arr))  # 1 | O(n)
arr.sort()  # O(n log n) average/worst for Python sort
arr.sort(reverse=True)  # O(n log n)
arr.reverse()  # O(n) in-place reverse
print(arr)  # [1, 2, 3, 4, 5, 6, 7]

# Copying array: reference vs shallow copy
newArr = arr  # O(1) -> same object (alias/reference)
anotherNewArr = arr[:]  # O(n) -> new list copy
print(newArr is arr)  # True  (same object)
print(anotherNewArr is arr)  # False (different object)

#Things to look out for
# 1) Index boundaries:
#    first index = 0
#    last index = len(arr) - 1
#    common bug: using len(arr) as last index

# 2) Time complexity quick memory:
#    append(), pop() end -> O(1)
#    insert/remove/pop(i) middle/start -> O(n)
#    x in arr, arr.index(x) -> O(n)
#    sort() -> O(n log n)

# 3) Slicing facts:
#    arr[a:b] returns a new list (copy)
#    arr[::-1] returns reversed new list
#    slicing uses extra space

# 4) append vs extend:
#    arr.append([8, 9]) -> adds one nested element
#    arr.extend([8, 9]) -> adds 8 and 9 separately

# 5) remove vs pop:
#    remove(x) removes by VALUE (first match)
#    pop(i) removes by INDEX and returns removed value

# 6) Safe looping:
#    avoid modifying list while iterating over same list
#    if needed, iterate over copy: for x in arr[:]


# 7) Edge cases to always test:
#    empty list []
#    one element [x]
#    duplicates
#    all same values
#    sorted and reverse-sorted input