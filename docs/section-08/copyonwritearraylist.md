# CopyOnWriteArrayList

## 1. Concept explanation
`CopyOnWriteArrayList` is a thread-safe list optimized for read-mostly workloads. Writes copy the entire backing array.

Iteration happens over a snapshot, so iterators do not throw ConcurrentModificationException.

## 2. Problem statement
Support safe iteration under concurrent reads while keeping reads lock-free.

## 3. Algorithm intuition
Great when reads >> writes (config lists, listeners). Terrible for write-heavy workloads due to copying.

## 4. Java 8 implementation
```java
import java.util.*;
import java.util.concurrent.*;

public class COWDemo {
    public static void main(String[] args) {
        CopyOnWriteArrayList<String> xs = new CopyOnWriteArrayList<>(Arrays.asList("a", "b"));
        for (String s : xs) {
            if ("a".equals(s)) xs.add("c");
        }
        System.out.println(xs);
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
- Input: ["a","b"], add "c" during iteration

## 7. Execution steps
- Iterate snapshot
- Write copies array
- Print list

## 8. Output
- Output: [a, b, c]

## 9. Time and space complexity
- read: O(1)
- write: O(n) copy

## 10. Enterprise relevance
Common for listener registries and configuration snapshots. Avoid for frequently-updated lists.

## 11. Interview discussion points
- Snapshot iteration
- Why no CME
- When it’s a bad choice

## 12. Best practices
- Use for read-mostly
- Avoid large lists
- Consider alternatives (ReadWriteLock)
