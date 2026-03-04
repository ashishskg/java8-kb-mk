# LinkedHashSet

## 1. Concept explanation
`LinkedHashSet` preserves insertion order while maintaining HashSet-like membership performance.

## 2. Problem statement
Deduplicate while preserving the first-seen order for stable API responses.

## 3. Algorithm intuition
Hash table + linked list of entries => deterministic iteration order.

## 4. Java 8 implementation
```java
import java.util.*;

public class LinkedHashSetDemo {
    public static void main(String[] args) {
        Set<String> s = new LinkedHashSet<>(Arrays.asList("b", "a", "b", "c"));
        System.out.println(s);
    }
}
```

## 5. Stream API implementation
```java
import java.util.*;
import java.util.stream.*;

public class LinkedHashSetStream {
    public static void main(String[] args) {
        List<String> xs = Arrays.asList("b", "a", "b", "c");
        Set<String> s = xs.stream().collect(Collectors.toCollection(LinkedHashSet::new));
        System.out.println(s);
    }
}
```

## 6. Sample input
- Input: ["b","a","b","c"]

## 7. Execution steps
- Insert while keeping links
- Iterate in insertion order

## 8. Output
- Output: [b, a, c]

## 9. Time and space complexity
- Time: O(1) avg membership
- Space: O(n)

## 10. Enterprise relevance
Stable iteration order avoids flaky tests and ensures deterministic JSON output.

## 11. Interview discussion points
- How order is preserved
- LinkedHashSet vs HashSet

## 12. Best practices
- Use for deterministic ordering
- Avoid if you don’t need order
