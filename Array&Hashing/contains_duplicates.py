''we use two nested loops, the outer loop to pick each element, the inner loop to compare this element with its subsequent elments
if found to be  equal we simply return True, else we complete traversing the array, we return False'''
# Time Complexity: O(n^2)
# Space Complexity: O(1)
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]:
            return True
return False



'''
The second approach 
we first sort the array, if any duplicates are present, they appear consecutively, so using a loop we check consecutive elements, if found same
we return True, otherwise return False'''
# Time Complexity: O(n log n)
# Space Complexity: O(n) — due to internal sorting (depending on implementation)
nums.sort()
for i in range(1, len(nums)):
    if nums[i] == nums[i - 1]:
        return True
return False



'''
We use a hashset to keep track of elements seen so far, as we iterate, we will check if the current element is already present in the set, 
if yes we return True, otherwise we add it to the set, this is an effeicient with average lookup and insertion of O(1)Tc'''
# Time Complexity: O(n)
# Space Complexity: O(n)
hs = set()
for num in nums:
    if num in hs:
        return True
    hs.add(num)
return False
