# merge

## 1. Concept explanation
Java 8 Map method `merge` reduces boilerplate map-update code.

## 2. Problem statement
Update counters and defaults safely without containsKey/get/put patterns.

## 3. Algorithm intuition
Centralize update logic in one atomic-ish call (still understand ConcurrentHashMap guarantees).

## 4. Java 8 implementation
```java
import java.util.*;

public class MapApiDemo {
    public static void main(String[] args) {
        Map<String, Integer> m = new LinkedHashMap<>();
        m.put("a", 1);
        m.merge("a", 5, Integer::sum);
        if (!"".equals("")) {
            // stdout already printed by op
        }
        System.out.println(m);
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
- Input: before = {a=1}
- Input: operation = merge

## 7. Execution steps
- Initialize map
- Run merge
- Print after

## 8. Output
- Output: stdout = (none)
- Output: after = {a=6}
- Output note: Great for counters; merges existing with new value.

## 9. Time and space complexity
- Time: O(1) average
- Space: O(1)

## 10. Enterprise relevance
Common in caches, aggregation maps, and counters. Avoid expensive remapping functions.

## 11. Interview discussion points
- computeIfAbsent vs putIfAbsent
- merge vs compute
- ConcurrentHashMap semantics

## 12. Best practices
- Keep functions pure
- Avoid heavy work in computeIfAbsent
