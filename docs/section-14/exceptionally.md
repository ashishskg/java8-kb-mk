# exceptionally

## 1. Concept explanation
`exceptionally` provides a fallback value when a stage completes exceptionally.

## 2. Problem statement
Return a default value when parsing fails.

## 3. Algorithm intuition
Handle exceptions close to where they can occur, or map them to domain errors.

## 4. Java 8 implementation
```java
import java.util.concurrent.*;

public class ExceptionallyDemo {
    public static void main(String[] args) {
        CompletableFuture<Integer> cf = CompletableFuture.supplyAsync(() -> "x")
                .thenApply(Integer::parseInt)
                .exceptionally(ex -> -1);
        System.out.println(cf.join());
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
- Input: "x" (invalid int)

## 7. Execution steps
- supplyAsync
- thenApply parse (throws)
- exceptionally fallback
- join

## 8. Output
- Output: -1

## 9. Time and space complexity
- N/A (concept)

## 10. Enterprise relevance
Critical for resilient clients. Decide if fallback is acceptable or you must propagate errors.

## 11. Interview discussion points
- exceptionally vs handle
- Where exception is caught

## 12. Best practices
- Don’t swallow errors silently
- Add metrics/logging
- Map to domain errors
