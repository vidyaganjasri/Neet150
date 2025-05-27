# ✅ Deep Dive: Second Approach – One-Pass HashMap Solution

This method improves readability and slightly optimizes performance by validating all three conditions in a **single traversal** of the board.

We aim to check:

- Row duplicates  
- Column duplicates  
- 3x3 Sub-grid duplicates  
→ all in just **one loop** over all 81 cells.

---

## 🔹 Step 1: Initialize Data Structures

We use three hash maps (dictionaries) where:

- `row[r]` stores all values in the r-th row  
- `col[c]` stores all values in the c-th column  
- `square[(r//3, c//3)]` stores all values in the 3x3 box that the cell belongs to

Each of these hash maps maps an index to a `set` of seen digits.

```python
from collections import defaultdict

row = defaultdict(set)
col = defaultdict(set)
square = defaultdict(set)
```

## 🔹 Step 2: Loop Over Every Cell in the Grid

```python
for r in range(9):
    for c in range(9):
```
For each cell:

- If it's empty (.), we skip it

- Otherwise, we check for violations in:

  -- The current row → row[r]

  -- The current column → col[c]

  -- The current sub-grid → square[(r//3, c//3)]

```python
if board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in square[(r//3, c//3)]:
    return False
```
If no violations are found, we add the value:

```python
row[r].add(board[r][c])
col[c].add(board[r][c])
square[(r//3, c//3)].add(board[r][c])
```

### 🧠 Why (r // 3, c // 3) for the square?
Just like in the first approach where we computed (square // 3) * 3 and (square % 3) * 3, here we let the cell itself tell us which square it's in.

Dividing row and column by 3 gives us the square grid it belongs to.

Example:
Cell (4, 5) → belongs to sub-grid (1, 1)

Using this coordinate pair as a dictionary key helps us efficiently group and track values by their 3x3 sub-box.

### 🧾 Skip Empty Cells
If the value is ".", we simply continue.
This avoids false positives from empty cells.

### ✅ Conclusion
The beauty of this approach is that everything is checked in one loop.

- It's clean, readable, and efficient.

- If a duplicate is found in any row, column, or box → return False

- If no duplicates are found after the full traversal → return True

### 🗣️ How to Say It in an Interview (Polished Version)
In my second approach, I validate the Sudoku board in a single pass using three hash maps.

I use a row dictionary, col dictionary, and square dictionary to track values seen in each row, column, and 3x3 subgrid.

As I iterate through every cell, I skip empty ones. For the rest, I check whether the value already exists in the corresponding row, column, or square set. If it does, I return False.

For squares, I use the (r // 3, c // 3) coordinate as the key, which uniquely identifies each of the 9 sub-boxes.

This approach is concise and ensures all three constraints are checked at once. If the board passes the full scan without any conflict, I return True.

