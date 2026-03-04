# HashMap Java 8 Improvements

## 1. Concept explanation
Java 8 improved HashMap under high collision by introducing *tree bins* (bucket can become a tree) and also added richer Map APIs (`computeIfAbsent`, `merge`, etc.).

Practical impact: worst-case performance improves, and common update patterns become less error-prone.

## 2. Problem statement
Build a frequency map safely and concisely using Java 8 Map APIs.

## 3. Algorithm intuition
Use `merge` for counters and `computeIfAbsent` for initializing collections.

## 4. Java 8 implementation
```java
import java.util.*;

public class MapImprovements {
    public static void main(String[] args) {
        List<String> xs = Arrays.asList("a", "b", "a");
        Map<String, Integer> freq = new HashMap<>();
        for (String s : xs) {
            freq.merge(s, 1, Integer::sum);
        }
        System.out.println(freq);

        Map<String, List<String>> groups = new HashMap<>();
        groups.computeIfAbsent("k", k -> new ArrayList<>()).add("v1");
        System.out.println(groups);
    }
}
```

## 5. Stream API implementation
```java
import java.util.*;
import java.util.stream.*;

public class FreqStream {
    public static void main(String[] args) {
        List<String> xs = Arrays.asList("a", "b", "a");
        Map<String, Long> freq = xs.stream().collect(Collectors.groupingBy(s -> s, Collectors.counting()));
        System.out.println(freq);
    }
}
```

## 6. Sample input
- Input: ["a","b","a"]
- Input: computeIfAbsent("k").add("v1")

## 7. Execution steps
- Use merge for counters
- Use computeIfAbsent for multi-map
- Print maps

## 8. Output
- Output: {a=2, b=1}
- Output: {k=[v1]}
- Output: {a=2, b=1} (stream)

## 9. Time and space complexity
- Time: O(n)
- Space: O(n)

## 10. Enterprise relevance
Map API methods reduce race-prone and bug-prone update code, especially with ConcurrentHashMap.

## 11. Interview discussion points
- merge vs compute
- computeIfAbsent pitfalls
- tree bins conceptually

## 12. Best practices
- Keep remapping functions pure
- Avoid heavy work inside computeIfAbsent
- Prefer merge for counters
