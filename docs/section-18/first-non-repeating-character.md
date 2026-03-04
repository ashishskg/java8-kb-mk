# First Non-Repeating Character

## 1. Concept explanation
Find the first character that occurs exactly once.

## 2. Problem statement
Given s, return index of first non-repeating character, or -1.

## 3. Algorithm intuition
Count frequencies, then scan again to find first char with count==1.

## 4. Java 8 implementation
```java
import java.util.*;

public class FirstUniqueChar {
    public static int firstUnique(String s) {
        int[] cnt = new int[256];
        for (int i = 0; i < s.length(); i++) cnt[s.charAt(i)]++;
        for (int i = 0; i < s.length(); i++) {
            if (cnt[s.charAt(i)] == 1) return i;
        }
        return -1;
    }

    public static void main(String[] args) {
        System.out.println(firstUnique("leetcode"));
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
- Input: "leetcode"

## 7. Execution steps
- Count frequencies
- Second pass find first count==1

## 8. Output
- Output: 0

## 9. Time and space complexity
- Time: O(n)
- Space: O(1) for fixed alphabet

## 10. Enterprise relevance
Useful in log analysis and token parsing; confirm character set requirements.

## 11. Interview discussion points
- Two-pass approach
- LinkedHashMap alternative

## 12. Best practices
- Clarify charset
- Use LinkedHashMap for Unicode-safe frequency tracking
