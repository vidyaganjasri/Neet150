## My Explanation

The given problem is to find the **longest consecutive sequence** from an **unsorted array**. Regardless of the position of elements, we are only supposed to focus on the **consecutive elements**.

### Example:
If the given input array is `[4, 6, 2, 3]`,  
the longest consecutive sequence is `3`, which is `2, 3, 4`.

To solve this problem, there are three approaches:

---

### 1. Brute Force Approach

- Traverse the array, and for each current element, assume it to be the **start of a sequence**.
- Use a `while` loop to look for its **consecutive elements** by incrementing the `curr` value.
- For each consecutive number found, **update the sequence length** and track the `max_length`.
- Repeat this process for **every element** in the array.

Before this, create a **set** from the array for:
- Efficient lookup operations.
- Avoiding redundant searches.

**Time Complexity**: `O(N^2)`  
**Space Complexity**: `O(N)` (due to the HashSet)

```python
nums_set = set(nums)
        max_length = 0 
        for i in range(len(nums)):
            curr,streak = nums[i],0 
            while curr in nums_set:
                streak +=1 
                curr+=1
            max_length = max(max_length,streak)
        return max_length
```

---

### 2. Sorting-Based Approach

This approach eliminates the need for nested loops and reduces unnecessary checks.

- **Sort** the elements first.
- Initialize two variables: `streak` and `max_streak` to `1`.
- Start from the second element (index `1`) and handle three conditions:
  - If `nums[i] == nums[i - 1]`: It's a duplicate, so continue.
  - Else if `nums[i] == nums[i - 1] + 1`: It's a consecutive element — update `streak` and `max_streak`.
  - Else: Reset `streak` to `1`, indicating a break in the sequence.

**Time Complexity**: `O(N log N)` (due to sorting)  
**Space Complexity**: `O(1)` (ignoring internal sorting space)
```python
if len(nums)<=1:
            return len(nums)
        
        streak = 1 
        max_streak = 1

        nums.sort()
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                continue 
            elif nums[i]==nums[i-1]+1:
                streak+=1 
                max_streak = max(streak,max_streak)
            else:
                streak = 1
            
        return max_streak 
```


---

### 3. Optimal HashSet-Based Approach

This is the most efficient and recommended approach.

- Create a **set** from the input array for fast lookup.
- Traverse the set, and for each element:
  - Check if `num - 1` exists in the set.
    - If it does, skip (as it's not the start of a sequence).
    - If it doesn’t, it's a **starting point** of a new sequence.
- Initialize `current_num` and `streak` to `1`.
- Use a `while` loop to check for `current_num + 1` in the set.
  - If found, increment both `current_num` and `streak`.
- After the loop, **update the max sequence length** if necessary.

**Time Complexity**: `O(N)`  
**Space Complexity**: `O(N)`

```python
max_streak = 0
        nums_set = set(nums)
        for n in nums_set:
            if n-1 in nums_set:
                continue
            else:
                streak = 1
                curr = n+1
                while curr in nums_set:
                    streak+=1 
                    curr+=1 
                max_streak = max(streak,max_streak)
        return max_streak 

```

---
