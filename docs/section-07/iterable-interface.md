# Iterable Interface

## 1. Concept explanation
`Iterable` is the root that enables the enhanced for-loop and provides `iterator()`.

## 2. Problem statement
Implement a custom iterable and iterate safely.

## 3. Algorithm intuition
Expose iteration via `Iterator` without exposing internal representation.

## 4. Java 8 implementation
```java
import java.util.*;

class Range implements Iterable<Integer> {
    private final int start, endInclusive;
    Range(int start, int endInclusive) { this.start = start; this.endInclusive = endInclusive; }

    public Iterator<Integer> iterator() {
        return new Iterator<Integer>() {
            int cur = start;
            public boolean hasNext() { return cur <= endInclusive; }
            public Integer next() { return cur++; }
        };
    }
}

public class IterableDemo {
    public static void main(String[] args) {
        for (int x : new Range(1, 3)) System.out.println(x);
    }
}
```

## 5. Stream API implementation
```java
import java.util.*;
import java.util.stream.*;

public class IterableStream {
    public static void main(String[] args) {
        Iterable<Integer> it = Arrays.asList(1,2,3);
        // Streams require a Collection or Spliterator; most Iterables are Collections in practice.
        List<Integer> out = StreamSupport.stream(it.spliterator(), false)
                .map(x -> x * 2)
                .collect(Collectors.toList());
        System.out.println(out);
    }
}
```

## 6. Sample input
- Input: Range(1..3)

## 7. Execution steps
- Implement iterator()
- Use for-each
- (Optional) Stream via spliterator

## 8. Output
- Output: 1
- Output: 2
- Output: 3

## 9. Time and space complexity
- Time: O(n) iteration
- Space: O(1)

## 10. Enterprise relevance
Useful for exposing domain-specific iteration without leaking internal collections (e.g., paged results wrappers).

## 11. Interview discussion points
- Iterable vs Iterator
- Why Iterator is stateful
- Spliterator basics

## 12. Best practices
- Don’t return null iterators
- Document iteration order
- Prefer immutability
