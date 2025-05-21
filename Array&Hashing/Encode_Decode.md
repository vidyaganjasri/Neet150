# Encode and Decode Strings — Complete Explanation

---

## Problem Statement

Implement two functions:

- `encode(strs: List[str]) -> str`: Converts a list of strings into a single string.
- `decode(s: str) -> List[str]`: Converts the encoded single string back into the original list.

---

## Naive Approach: Using a Delimiter

- Join all strings with a special delimiter like `"#"` or `"|"`.
- **Problem:** If any original string contains the delimiter itself, decoding becomes ambiguous and can produce incorrect results.
- Hence, this approach is unreliable for arbitrary input strings.

---

## Robust Approach: Length-Prefixed Encoding

- Encode each string by prefixing its length, followed by a delimiter (`#`), then the string itself.
- This method avoids ambiguity because the length indicates exactly how many characters to read.
- It works correctly even if strings contain the delimiter or are empty.

---

## Encoding Logic

- For each string, append:
  - The length of the string (as a string)
  - A delimiter `#`
  - The string itself
- Concatenate all these segments to form the encoded string.

---

## Decoding Logic

- Initialize a pointer to iterate over the encoded string.
- While the pointer is within the string length:
  1. Find the next `#` delimiter to determine the substring that indicates the length.
  2. Convert this substring to an integer to get the length of the next string.
  3. Extract the string of the given length immediately following the delimiter.
  4. Append the extracted string to the result list.
  5. Move the pointer forward past the extracted string to decode the next segment.

---

```py
def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        for val in strs:
            res+= str(len(val))+"#"+val
        return res

        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        res,i = [],0
        while i<len(s):
            j = i
            while s[j]!="#":
                j+=1
            length = int(s[i:j])
            val = s[j+1:j+1+length]
            res.append(val)
            i = j+1+length
        return res
```

## Time Complexity

- **Encoding:** O(N), where N is the total length of all input strings combined.  
  Each character is processed once to build the encoded string.

- **Decoding:** O(N), where N is the length of the encoded string.  
  Each character is processed once to identify lengths and extract strings.

---

## Summary

| Approach             | Advantages                   | Disadvantages                 |
|----------------------|------------------------------|-------------------------------|
| Naive (delimiter)    | Simple implementation         | Fails if delimiter appears in strings |
| Length-prefixed (robust) | Unambiguous and reliable      | Slightly more complex encoding/decoding |

---

This length-prefixed approach ensures correct encoding and decoding of any list of strings regardless of their content.
