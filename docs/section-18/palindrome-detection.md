# Palindrome Detection

## 1. Concept explanation
A palindrome reads the same forward and backward.

## 2. Problem statement
Given s, return true if it is a palindrome (exact match).

## 3. Algorithm intuition
Two pointers compare from ends; early-exit on mismatch.

## 4. Java 8 implementation
```java
public class Palindrome {
    public static boolean isPal(String s) {
        int i = 0, j = s.length() - 1;
        while (i < j) {
            if (s.charAt(i) != s.charAt(j)) return false;
            i++; j--;
        }
        return true;
    }
    public static void main(String[] args) {
        System.out.println(isPal("abba"));
        System.out.println(isPal("abca"));
    }
}
```

## 5. Stream API implementation
```java
import java.util.*;
import java.util.stream.*;

public class Example {
    public static void main(String[] args) {
        List<Integer> xs = Arrays.asList(1, 2, 3, 4, 5);
        int sumOfEvens = xs.stream().filter(x -> x % 2 == 0).mapToInt(x -> x).sum();
        System.out.println(sumOfEvens);
    }
}
```

## 6. Sample input
- Input: "abba"
- Input: "abca"

## 7. Execution steps
- Compare ends
- Move inward
- Early exit on mismatch

## 8. Output
- Output: true
- Output: false

## 9. Time and space complexity
- Time: O(n)
- Space: O(1)

## 10. Enterprise relevance
Often used in validation rules; variants include ignoring non-alphanumerics and case.

## 11. Interview discussion points
- Two pointers
- Variants (ignore punctuation/case)

## 12. Best practices
- Clarify normalization rules
- Avoid building reversed copies if not needed
