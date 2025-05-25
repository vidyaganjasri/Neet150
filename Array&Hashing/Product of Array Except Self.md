# Product of Array Except Self — Explanation

The problem asks us to return an array where each element at index `i` is the product of all elements in the input array except the one at index `i`.

There are three approaches to solve this problem, each with different time and space complexities.

---

## 1. Brute Force Approach

In this method, we use two nested loops:

- The outer loop iterates over each element of the array.
- The inner loop computes the product of all elements excluding the current index.
- We simply skip the current index during multiplication using a condition like `if i == j, continue`.

**Time Complexity:** O(N²)  
**Space Complexity:** O(1), since we don’t use any extra space.

```py
ans = []
        for i in range(len(nums)):
            k = 1
            for j in range(len(nums)):
                if i==j:
                    continue
                else:
                    k *= nums[j]
            ans.append(k)
        return ans
```

---

## 2. Prefix and Suffix Arrays Approach

This approach works in O(N) time complexity, and uses auxiliary space of O(N).

- Compute a **prefix product array** that stores the product of all elements to the left of the current index.
- Compute a **suffix product array** that stores the product of all elements to the right of the current index.
- Once both arrays are built, multiply the corresponding elements of the prefix and suffix arrays to get the final result.

```py
pref = [1]*len(nums)
        suff = [1]*len(nums)

        #calculating pref array 
        for i in range(1,len(nums)):
            pref[i] = pref[i-1]*nums[i-1]
        
        for j in range(len(nums)-2,-1,-1):
            suff[j] = suff[j+1]*nums[j+1]
        
        ans = [1]*len(nums)
        for i in range(len(nums)):
            ans[i] = pref[i]*suff[i]
        return ans
```


---

## 3. Optimal Approach (Using Variables)

This is the optimal approach, which works in O(N) time complexity, and uses O(1) auxiliary space, if we don’t count the output array.

- Unlike the second approach that uses two extra arrays, here we use just two variables — a **prefix** and a **suffix** — to compute the result.
- This method involves two passes:
  - In the first pass, we iterate from left to right and build the result array using the prefix product.
  - In the second pass, we traverse from right to left, maintaining the suffix product and multiplying it with the current value in the result array.
- This gives us the final output without needing any extra space apart from the output array itself.

```py
ans = [1]*len(nums)
        pref = 1 
        for i in range(len(nums)):
            ans[i]=pref 
            pref*=nums[i]
        
        suff = 1
        for i in range(len(nums)-1,-1,-1):
            ans[i]*=suff
            suff*=nums[i]
        return ans 
```


# Real-Life Examples of "Product of Array Except Self"

### Team work:
You have a team and each person works hard. You want to know how much work the rest of the team did if you don’t count one person.

### System parts:
A machine has many parts, and its total performance depends on all parts working well. You want to see how well the machine works if one part is removed.

### Investments:
You have several investments, and the total money grows because of all of them. You want to check how much the portfolio grows if you take out one investment.

### Factory process:
A product goes through many steps in a factory, and each step affects how many good products are made. You want to find out the total good products if one step didn’t happen.
