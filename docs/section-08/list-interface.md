# List Interface

## 1. Concept explanation
`List` is an ordered collection that allows duplicates and supports positional access.

Common implementations:
- ArrayList: fast random access
- LinkedList: fast adds/removes near ends (but poor locality)
- CopyOnWriteArrayList: read-mostly concurrency

## 2. Problem statement
Pick the right List implementation for read-heavy vs write-heavy workloads.

## 3. Algorithm intuition
Choose by operations: random access -> ArrayList; frequent inserts/removals in middle -> usually still ArrayList unless proven otherwise; concurrent read-mostly -> CopyOnWriteArrayList.

## 4. Java 8 implementation
```java
import java.util.*;

public class ListBasics {
    public static void main(String[] args) {
        List<String> xs = new ArrayList<>();
        xs.add("a");
        xs.add("b");
        xs.add(1, "x");
        System.out.println(xs);
        System.out.println(xs.get(0));
    }
}
```

## 5. Stream API implementation
```java
import java.util.*;
import java.util.stream.*;

public class ListStream {
    public static void main(String[] args) {
        List<String> xs = Arrays.asList(" a ", "b", "");
        List<String> out = xs.stream().map(String::trim).filter(s -> !s.isEmpty()).collect(Collectors.toList());
        System.out.println(out);
    }
}
```

## 6. Sample input
- Input: add a,b then add(1,"x")
- Input: [" a ","b",""]

## 7. Execution steps
- Use positional add/get
- Normalize via stream
- Collect

## 8. Output
- Output: [a, x, b]
- Output: [a, b]

## 9. Time and space complexity
- get/set by index: O(1) for ArrayList, O(n) for LinkedList
- insert at index: O(n)

## 10. Enterprise relevance
List choice affects latency and memory; ArrayList is the default in most services due to cache locality.

## 11. Interview discussion points
- ArrayList vs LinkedList
- Random access cost
- Fail-fast iterators

## 12. Best practices
- Program to List
- Prefer ArrayList by default
- Avoid LinkedList unless measured
