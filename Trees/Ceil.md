```python
class Solution:
    def findCeil(self,root, inp):
        # code here
        c = -1 
        while root:
            if root.key == inp:
                return inp
            elif inp>root.key:
                root = root.right 
            elif inp<root.key:
                c = root.key
                root=root.left
        return c
```
