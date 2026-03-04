# counting

## 1. Concept explanation
`counting()` is a downstream collector that counts elements (often used with groupingBy).

## 2. Problem statement
Count requests per endpoint.

## 3. Algorithm intuition
Counting is O(1) per element; combine it with groupingBy for one-pass aggregation.

## 4. Java 8 implementation
```java
import java.util.*;

public class Example {
    public static void main(String[] args) {
        List<Integer> xs = Arrays.asList(1, 2, 3, 4, 5);
        int sum = 0;
        for (int x : xs) sum += x;
        System.out.println(sum);
    }
}
```

## 5. Stream API implementation
```java
import java.util.*;
import java.util.stream.*;

public class CountingDemo {
    public static void main(String[] args) {
        List<String> paths = Arrays.asList("/a", "/b", "/a");
        Map<String, Long> counts = paths.stream()
                .collect(Collectors.groupingBy(p -> p, Collectors.counting()));
        System.out.println(counts);
    }
}
```

## 6. Sample input
- Input: ["/a","/b","/a"]

## 7. Execution steps
- groupingBy(path, counting)
- Print map

## 8. Output
- Output: {/a=2, /b=1}

## 9. Time and space complexity
- Time: O(n)
- Space: O(n)

## 10. Enterprise relevance
Used for metrics and log analysis; be mindful of high-cardinality keys.

## 11. Interview discussion points
- count() terminal vs counting() collector
- cardinality concerns

## 12. Best practices
- Control cardinality
- Consider approximate counting for huge domains
