# Longest Substring Without Repeating Characters

## 1. Concept explanation
Find the longest substring with all unique characters.

## 2. Problem statement
Given s, return length of longest substring with no repeated characters.

## 3. Algorithm intuition
Sliding window with a set/map: expand right; shrink left until unique.

## 4. Java 8 implementation
```java
import java.util.*;

public class LongestUniqueSubstring {
    public static int length(String s) {
        Set<Character> win = new HashSet<>();
        int best = 0;
        int l = 0;
        for (int r = 0; r < s.length(); r++) {
            char c = s.charAt(r);
            while (win.contains(c)) {
                win.remove(s.charAt(l));
                l++;
            }
            win.add(c);
            best = Math.max(best, r - l + 1);
        }
        return best;
    }

    public static void main(String[] args) {
        System.out.println(length("abcabcbb"));
    }
}
```

## 5. Stream API implementation
```java
public class LongestUniqueStreamNote {
    // Sliding window is stateful; streams are not a good fit.
}
```

## 6. Sample input
- Input: "abcabcbb"

## 7. Execution steps
- Expand right pointer
- If repeat, shrink left
- Track best window

## 8. Output
- Output: 3

## 9. Time and space complexity
- Time: O(n)
- Space: O(min(n, alphabet))

## 10. Enterprise relevance
Used in rate-limiting token parsing, uniqueness constraints, and window-based analytics.

## 11. Interview discussion points
- Why O(n)
- Set vs last-seen index map optimization

## 12. Best practices
- Use last-seen index map for faster shrink
- Clarify character set (ASCII/Unicode)
