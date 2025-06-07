# Question

Given a **sorted array**, find two numbers that add up to a target value.  
For example, in `[1, 2, 7, 8]`, if the target is `9`, the pair `(2, 7)` sums up to the target.

---

# Approaches to Solve the Problem

### 1. Brute Force (Nested Loops)
```python
for i in range(len(numbers)):
            for j in range(i+1,len(numbers)):
                if numbers[i]+numbers[j]==target:
                    return [i+1,j+1]
```
- Iterate through each element with two nested loops, checking every pair to see if their sum equals the target.

**Time Complexity:** O(N²)  
**Space Complexity:** O(1)

---

### 2. Binary Search

- For each element `arr[i]`, calculate `target - arr[i]` and use binary search on the remaining elements to find this value. This leverages the fact that the array is sorted.
```python
def bin_search(left,right,b):
            while left<=right:
                mid = (left+right)//2
                if numbers[mid]==b:
                    return mid
                elif numbers[mid]>b:
                    right = mid-1
                else:
                    left = mid+1
                
            return -1 

        for i in range(len(numbers)):
            b = target -  numbers[i]
            ind = bin_search(i+1,len(numbers)-1,b)
            if ind!=-1:
                return [i+1,ind+1]
```
**Time Complexity:** O(N log N)  
**Space Complexity:** O(1)

---

### 3. Hash Map
```python
 hm = {}
        for i in range(len(numbers)):
            if target - numbers[i] in hm.items():
                return [hm[target-numbers[i]]+1,i+1]
            else:
                hm[numbers[i]] = i
```
- Traverse the array once, storing each element and its index in a hashmap.
- For each element, check if `target - element` exists in the hashmap. If yes, return the indices.
- This method works regardless of sorting.

**Time Complexity:** O(N)  
**Space Complexity:** O(N)

---

### 4. Two-Pointer Technique (Most Efficient for Sorted Arrays)
```python
 left = 0 
        right = len(numbers)-1
        while numbers[left]+numbers[right]!=target:
            if numbers[left]+numbers[right]>target:
                right-=1
            else:
                left+=1
        return [left+1,right+1]
```
- Initialize two pointers — one at the start (`left`), one at the end (`right`).
- Calculate the sum of elements at these pointers:
  - If the sum equals the target, return their indices.
  - If the sum is greater than the target, move the `right` pointer left.
  - If the sum is less than the target, move the `left` pointer right.
- Repeat until pointers meet or the pair is found.

**Time Complexity:** O(N)  
**Space Complexity:** O(1)
