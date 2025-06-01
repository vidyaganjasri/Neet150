# Palindrome Validation Problem

The problem is to determine whether the given string is a **valid palindrome**.  
A string is considered a palindrome if it reads the same forward and backward.

**For example:**  
- `"eye"`  
- `"maam"`

However, in this version of the problem, we need to **ignore all non-alphanumeric characters** and **treat uppercase and lowercase letters as equal**.

---

## Approach 1: Filtering and Reverse

We iterate through the original string, extract only the alphanumeric characters, and convert them to lowercase to build a filtered string.  
At the end, we check whether this filtered string is equal to its reverse.

- **Time Complexity:** O(N), where N is the length of the string  
- **Space Complexity:** O(N), for storing the filtered string

---

```python
def funct(str s):
  new_str = ''
  for c in s:
      if c.isalnum():
          new_str+=c.lower()
  return new_str==new_str[::-1]
```

## Approach 2: Two-Pointer Technique (Space-Efficient)

This approach is more efficient in terms of space.

We place two pointers — `left` at the start and `right` at the end of the string.  
At each step:

- If either character is **non-alphanumeric**, we move the respective pointer inward and continue.  
- If both characters are alphanumeric, we compare their **lowercase versions**:  
  - If they **match**, we move both pointers inward.  
  - If they **don’t match**, we return `False`, since it violates the palindrome condition.

We repeat this process until the `left` pointer is **strictly less than** the `right` pointer.

```python
if len(s)==0:
    return True 
l=0
r = len(s)-1
while l<r:
    if not s[l].isalnum():
        l+=1 
        continue
    if not s[r].isalnum():
        r-=1 
        continue
    if  s[l].lower()==s[r].lower():
        l+=1
        r-=1
    else:
        return False
return True
```

- **Time Complexity:** O(N)  
- **Space Complexity:** O(1), since we’re not using any extra space

---

This two-pointer approach is optimal, using constant space while maintaining linear time complexity, making it ideal for interview settings.
