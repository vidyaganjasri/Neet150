```python
def find_floor(root, key):
    floor = -1
    while root:
        if root.key == key:
            return root.key
        elif key < root.key:
            root = root.left
        else:
            floor = root.key
            root = root.right
    return floor
```
