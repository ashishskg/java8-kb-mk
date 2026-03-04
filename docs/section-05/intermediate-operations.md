# Intermediate Operations

## 1. Concept explanation
Intermediate operations are lazy: filter, map, flatMap, distinct, sorted, limit/skip, peek.

## 2. Problem statement
Apply common intermediate operations with deterministic outputs.

## 3. Algorithm intuition
Intermediate ops transform the stream; no work happens until a terminal op is invoked.

## 4. Java 8 implementation
```java
import java.util.*;

public class IntermediateOpsLoop {
    public static void main(String[] args) {
        List<Integer> xs = Arrays.asList(5,1,2,2,9);

        // E1 filter
        List<Integer> e1 = new ArrayList<>();
        for (int x : xs) if (x % 2 == 0) e1.add(x);
        System.out.println("E1=" + e1);

        // E2 map
        List<Integer> e2 = new ArrayList<>();
        for (int x : xs) e2.add(x * 10);
        System.out.println("E2=" + e2);

        // E3 distinct (manual)
        List<Integer> e3 = new ArrayList<>();
        for (int x : xs) if (!e3.contains(x)) e3.add(x);
        System.out.println("E3=" + e3);

        // E4 sorted
        List<Integer> e4 = new ArrayList<>(xs);
        Collections.sort(e4);
        System.out.println("E4=" + e4);

        // E5 limit
        System.out.println("E5=" + e4.subList(0, 3));

        // E6 skip
        System.out.println("E6=" + e4.subList(2, e4.size()));
    }
}
```

## 5. Stream API implementation
```java
import java.util.*;
import java.util.stream.*;

public class IntermediateOpsStream {
    public static void main(String[] args) {
        List<Integer> xs = Arrays.asList(5,1,2,2,9);
        System.out.println("E1=" + xs.stream().filter(x -> x % 2 == 0).collect(Collectors.toList()));
        System.out.println("E2=" + xs.stream().map(x -> x * 10).collect(Collectors.toList()));
        System.out.println("E3=" + xs.stream().distinct().collect(Collectors.toList()));
        System.out.println("E4=" + xs.stream().sorted().collect(Collectors.toList()));
        System.out.println("E5=" + xs.stream().sorted().limit(3).collect(Collectors.toList()));
        System.out.println("E6=" + xs.stream().sorted().skip(2).collect(Collectors.toList()));
    }
}
```

## 6. Sample input
- Input: [5,1,2,2,9]

## 7. Execution steps
- Apply each intermediate op
- Collect to trigger execution

## 8. Output
- Output: E1=[2, 2]
- Output: E2=[50, 10, 20, 20, 90]
- Output: E3=[5, 1, 2, 9]
- Output: E4=[1, 2, 2, 5, 9]
- Output: E5=[1, 2, 2]
- Output: E6=[2, 5, 9]

## 9. Time and space complexity
- filter/map/distinct: ~O(n) (distinct uses set)
- sorted: O(n log n)

## 10. Enterprise relevance
Intermediate ops are where most bugs happen: ordering, distinctness, and stateful lambdas.

## 11. Interview discussion points
- Why intermediate ops are lazy
- Stateful ops and memory
- peek usage

## 12. Best practices
- Avoid stateful lambdas
- Be explicit about order
- Use limit for safety
