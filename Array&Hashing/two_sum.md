# Problem Statement: 
Given an array called as num and a target value, we are supposed to return the 
indices of two numbers present in the array such that add up to the target value.

---

## Brute Force Approach(O(n^2))
First I'd go with the most straightforward approach which is the brute force 
approach using two nested loops, where I check each and every possible pair of 
elements to see if their sum equals the target, if so, I return their indices

```py
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            return [i, j]
```
TC: O(n^2) : since we are using two nested loops
SC: O(1) : no extra data structure is used
but this is ineffecient for large inputs 

---

## Sorting + Two Pointer(O(nlogn))

To improve the effeciency, I can store the values along with their original indices
in a list of tuples, sort it and using two pointer approach to find the target sum 
where we place two pointers left and right at the beginning and end of the list
and get the values acc and sum it up if found to be equal, we return the indices, else if
it is foudn to be greater then the target, we decrement the right pointer else 
we increment the right pointer.

```py
indexed_nums = [(num, i) for i, num in enumerate(nums)]
indexed_nums.sort()  # Sort based on values

left = 0
right = len(indexed_nums) - 1

while left < right:
    total = indexed_nums[left][0] + indexed_nums[right][0]
    if total == target:
        return [indexed_nums[left][1], indexed_nums[right][1]]
    elif total < target:
        left += 1
    else:
        right -= 1
```
TC: O(nlogn) + O(n)
for sorting and traversal 
SC: P(n) for storing the valeu, index paird 

---

## Hashmap O(n) optimal 

This is the most effecient solution, where as I keep traversing the array 
I check whether the complimentary which is target-currentnumber already 
exists in the hashmap, if yes, i return teh indices, if not I add the current 
number and index to its map


```py
hm = {}
for i, n in enumerate(nums):
    diff = target - n
    if diff in hm:
        return [hm[diff], i]
    hm[n] = i
```
tc: O(n)
SC:O(n)

---

# Real Time: 

If ur working in an ecommerce company and building a discount engine, 
and u want to add a feature, which allows you to find the item when placing in the cart 
would sum it up 1000, enabling the user to get combo discount.


