## Grouping_anagrams

### Problem statment
Basically the problem asks us to group strings that are anagrams of each other. 

---

## Explanation 

### Brute Force Approach 

The brute force approach would you two nested loops and a boolean array. The outer loop iterates the entire array, and for each element, the inner loop compares the it with the 
subsequent elements. If two strings are anagrams, we group them togeather. 
The boolean array helps mark which elements have already been grouped, so we don’t process them again.

```py
def is_anagram(s,t):
            return sorted(s)==sorted(t)
        
        bool_arr = [0]*len(strs)
        res= []
        for i in range(len(strs)):
            if bool_arr[i]==0:
                s = []
                s.append(strs[i])
                for j in range(i+1,len(strs)):
                    if is_anagram(strs[i],strs[j]):
                        s.append(strs[j])
                        bool_arr[j]=1
                bool_arr[i]=1
                res.append(s)

        return res
```
---

### Effecient Approach 

However, a more efficient approach uses a hash map. We iterate over the array once. For each string, we sort its characters — this sorted string becomes the key in the hash map. If the key already exists, we append the original string to its list; otherwise, we create a new key-value pair with the sorted string as the key and a list containing the original string as the value.

Finally, we return the list of values from the hash map, which represent the grouped anagrams.

```py
hm = {}
        for i in range(len(strs)):
            k = ''.join((sorted(strs[i])))
            if k not in hm.keys():
                hm[k] = [strs[i]]
            else:
                hm[k].append(strs[i])
        
        return [x for x in hm.values()]
```
---
## Time Complexity

In terms of time complexity:

The brute-force approach takes O(N² * K log K), where N is the number of strings and K is the average string length (because of sorting during comparisons).

The hash map approach runs in O(N * K log K) due to sorting each string once, and uses O(N * K) space for storing groups.
