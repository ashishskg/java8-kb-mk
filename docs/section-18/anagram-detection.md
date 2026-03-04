# Anagram Detection

## 1. Concept explanation
Two strings are anagrams if they contain the same characters with the same counts.

## 2. Problem statement
Given s and t, return true if they are anagrams.

## 3. Algorithm intuition
Count frequencies and compare. For lowercase a-z, use int[26].

## 4. Java 8 implementation
```java
public class Anagram {
    public static boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        int[] cnt = new int[26];
        for (int i = 0; i < s.length(); i++) {
            cnt[s.charAt(i) - 'a']++;
            cnt[t.charAt(i) - 'a']--;
        }
        for (int c : cnt) if (c != 0) return false;
        return true;
    }
    public static void main(String[] args) {
        System.out.println(isAnagram("listen", "silent"));
    }
}
```

## 5. Stream API implementation
```java
import java.util.*;
import java.util.stream.*;

public class AnagramStreamNote {
    public static void main(String[] args) {
        String s = "listen", t = "silent";
        String a = s.chars().sorted().mapToObj(c -> String.valueOf((char)c)).collect(Collectors.joining());
        String b = t.chars().sorted().mapToObj(c -> String.valueOf((char)c)).collect(Collectors.joining());
        System.out.println(a.equals(b));
    }
}
```

## 6. Sample input
- Input: s="listen"
- Input: t="silent"

## 7. Execution steps
- Count chars
- Compare counts

## 8. Output
- Output: true

## 9. Time and space complexity
- Time: O(n) (counting)
- Space: O(1) for fixed alphabet

## 10. Enterprise relevance
Used in dedupe/normalization pipelines; clarify normalization (case, spaces, Unicode).

## 11. Interview discussion points
- Counting vs sorting approach
- Unicode considerations

## 12. Best practices
- Prefer counting for fixed alphabet
- Normalize inputs at boundaries
