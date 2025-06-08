### 🔍 Problem Statement

We are given a **sorted array** and a **target value**, and are asked to find the **greatest value that is less than or equal to the target** — in other words, the **floor** of the target.

---

### 🧠 Approach

Since the array is sorted and we're searching for an element based on a condition, **Binary Search** is the most efficient approach. It leverages the sorted nature of the array and gives us results in **O(log n)** time.

---

### ⚙️ Binary Search with a Twist

We modify the standard binary search slightly:

- At each step, we compute the `mid` index.
- If `arr[mid] <= target`:
  - This is a **valid candidate for floor**, so we store it.
  - We move to the **right half** (`left = mid + 1`) to search for a better (greater but still valid) candidate.
- If `arr[mid] > target`:
  - This value is too large to be a floor.
  - So, we move **left** (`right = mid - 1`) to find smaller values.

---

### 📌 Handling Duplicates

This method is also effective when the array contains **duplicate values**, because it ensures we return the **last occurrence** that satisfies `arr[i] <= target`.

---

### 🧾 Edge Case

- If no element in the array is less than or equal to the target, we return `-1`.

---

### ⏱️ Time & Space Complexity

- **Time Complexity:** `O(log n)`
- **Space Complexity:** `O(1)`

---
## Code 
```python
def findFloor(self, arr, x):
        #Your code here
        def binSearch(left,right,target):
            f = -1
            while left<=right:
                mid = (left+right)//2
                if arr[mid]<=target:
                    f = mid 
                    left = mid+1
                else:
                    right = mid-1
            return f 
        return binSearch(0,len(arr)-1,x)
```
### ✅ Summary

Binary Search is ideal here because:
- The array is sorted.
- We're searching for a boundary condition (`≤ target`).
- It provides both efficiency and correctness, even in the presence of duplicates.
