# Collection Hierarchy

## 1. Concept explanation
The Collection Framework is centered around `Iterable` and `Collection`, with specializations like `List`, `Set`, and `Queue`.

ASCII (simplified):
Iterable
  └─ Collection
      ├─ List
      ├─ Set
      └─ Queue

## 2. Problem statement
Choose the right collection type for ordering, uniqueness, and access patterns.

## 3. Algorithm intuition
Pick by constraints: need duplicates/order -> List; uniqueness -> Set; FIFO -> Queue; key-value -> Map (separate hierarchy).

## 4. Java 8 implementation
```java
import java.util.*;

public class CollectionChoices {
    public static void main(String[] args) {
        List<String> list = Arrays.asList("a", "b", "a");
        Set<String> set = new HashSet<>(list);
        Queue<String> q = new ArrayDeque<>(list);

        System.out.println(list); // keeps duplicates + order
        System.out.println(set);  // unique, order not guaranteed
        System.out.println(q.remove()); // FIFO
    }
}
```

## 5. Stream API implementation
```java
import java.util.*;
import java.util.stream.*;

public class HierarchyStream {
    public static void main(String[] args) {
        List<String> xs = Arrays.asList("a", "b", "a");
        Set<String> uniq = xs.stream().collect(Collectors.toSet());
        System.out.println(uniq);
    }
}
```

## 6. Sample input
- Input: ["a","b","a"]

## 7. Execution steps
- Use List for order
- Convert to Set for uniqueness
- Use Queue for FIFO

## 8. Output
- Output: [a, b, a]
- Output: Set contains a,b
- Output: a

## 9. Time and space complexity
- Time: O(n) conversions
- Space: O(n)

## 10. Enterprise relevance
Correct collection choice impacts performance, memory, and correctness (e.g., uniqueness constraints, ordering in APIs).

## 11. Interview discussion points
- List vs Set
- Queue use cases
- Why Map is not a Collection

## 12. Best practices
- Program to interfaces
- Choose based on access patterns
- Be explicit about ordering
