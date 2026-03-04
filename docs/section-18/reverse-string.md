# Reverse String

## 1. Concept explanation
Reverse a string by swapping characters from both ends toward the center.

## 2. Problem statement
Given s, return reversed string.

## 3. Algorithm intuition
Two pointers i/j swap until i>=j.

## 4. Java 8 implementation
```java
public class ReverseString {
    public static String rev(String s) {
        char[] a = s.toCharArray();
        int i = 0, j = a.length - 1;
        while (i < j) {
            char t = a[i]; a[i] = a[j]; a[j] = t;
            i++; j--;
        }
        return new String(a);
    }

    public static void main(String[] args) {
        System.out.println(rev("abcd"));
    }
}
```

## 5. Stream API implementation
```java
import java.util.stream.*;

public class ReverseStreamNote {
    public static void main(String[] args) {
        String s = "abcd";
        String out = IntStream.range(0, s.length())
                .mapToObj(i -> s.charAt(s.length() - 1 - i))
                .collect(StringBuilder::new, StringBuilder::append, StringBuilder::append)
                .toString();
        System.out.println(out);
    }
}
```

## 6. Sample input
- Input: "abcd"

## 7. Execution steps
- Convert to char[]
- Swap i/j
- Build new String

## 8. Output
- Output: dcba

## 9. Time and space complexity
- Time: O(n)
- Space: O(n) for char array

## 10. Enterprise relevance
Common utility in parsing and transformations; pay attention to Unicode grapheme clusters in real products.

## 11. Interview discussion points
- Two-pointer technique
- String immutability

## 12. Best practices
- Use StringBuilder for many concatenations
- Clarify Unicode requirements
