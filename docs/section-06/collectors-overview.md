# Collectors Overview

## 1. Concept explanation
Collectors are reduction strategies for `Stream.collect(...)`. A Collector defines how to accumulate elements into a container or summary.

Key idea: Collectors let you do *one pass* aggregation (grouping, counting, joining) instead of multiple loops.

## 2. Problem statement
Compute multiple aggregates from a list of events (counts + CSV of unique categories).

## 3. Algorithm intuition
Pick the right collector (groupingBy/partitioningBy/toMap/joining/summarizing) and define key collision policies.

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

public class CollectorsOverview {
    public static void main(String[] args) {
        List<String> names = Arrays.asList("amy", "bob", "carl", "bob");
        Map<Integer, Long> counts = names.stream()
                .collect(Collectors.groupingBy(String::length, Collectors.counting()));
        String csv = names.stream().distinct().sorted().collect(Collectors.joining(","));
        System.out.println(counts);
        System.out.println(csv);
    }
}
```

## 6. Sample input
- Input: [amy, bob, carl, bob]

## 7. Execution steps
- groupingBy(length, counting)
- distinct + sorted + joining

## 8. Output
- Output: {3=3, 4=1}
- Output: amy,bob,carl

## 9. Time and space complexity
- Time: O(n log n) with sorting; O(n) without sorting
- Space: O(n)

## 10. Enterprise relevance
Collectors power reporting endpoints and batch aggregations; always decide key collision policies (toMap merge).

## 11. Interview discussion points
- collect vs reduce
- collector components
- parallel collector safety

## 12. Best practices
- Prefer one-pass collectors
- Be explicit about merge behavior
- Avoid collecting massive datasets into memory
