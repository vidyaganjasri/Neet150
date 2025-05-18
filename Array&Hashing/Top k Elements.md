# Problem: Top K Frequent Elements
## Goal:
Given an integer array nums and an integer k, return the k most frequent elements. The order of output does not matter.

--- 

### Approach 1: HashMap + Sorting (Brute Force-ish)
Use a HashMap (dictionary) to count the frequency of each element in nums.

- Keys: elements

- Values: frequency counts

Sort the items of this HashMap by frequency in descending order using:

```py
sorted_hm = sorted(hm.items(), key=lambda x: x[1], reverse=True)
```
Here, x[1] is the frequency.

The sorted result is a list of (element, frequency) pairs, ordered by frequency high → low.

Return the first k elements from the sorted list using list comprehension:

```py
return [sorted_hm[i][0] for i in range(k)]
```

### Time Complexity:
Counting frequencies: O(N)
Sorting by frequency: O(N log N)

- Total: O(N log N)

---
```py
hm = {}

for i in range(len(nums)):
    hm[nums[i]] = hm.get(nums[i],0)+1

sorted_hm = sorted(hm.items(), key = lambda x:x[1],reverse = True)

return [sorted_hm[i][0] for i in range(k)]
```

---

## Approach 2: HashMap + Min-Heap (Efficient)
Use a HashMap (Counter from collections works great) to count frequencies.

Create a min-heap to keep track of the top k frequent elements.

For each (element, frequency) in the HashMap:

Push the tuple (frequency, element) into the min-heap.

### Important: Python’s heapq is a min-heap and sorts tuples by the first element by default.
So by pushing (frequency, element), the heap is ordered by frequency, allowing efficient access to the smallest frequency element.

If the size of the heap exceeds k, pop the smallest frequency element from the heap.

After processing all items, the heap contains the k elements with the highest frequencies.

Extract and return the elements (second part of the tuples) from the heap:

```py
return [pair[1] for pair in min_heap]
```

## Code Snippet:
```py
from collections import Counter
import heapq

def topKFrequent(nums, k):
    hm = Counter(nums)
    min_heap = []

    for num, freq in hm.items():
        # Push tuple with frequency first so heap sorts by freq
        heapq.heappush(min_heap, (freq, num))
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    # Extract elements from the heap ignoring frequencies
    return [pair[1] for pair in min_heap]
```

### Time Complexity:
Counting frequencies: O(N)
Heap operations: O(N log k) (each push/pop is log k, done N times)

- Total: O(N log k) which is more efficient than sorting for large N and small k.


## real-life uses for top K frequent elements:

 Here’s a quick list of 
- Trending search queries on search engines

- Best-selling products on e-commerce sites

- Most liked/commented posts or hashtags on social media

- Frequent spam words or IP addresses in spam detection

- Most played songs or videos on streaming platforms
