# thenCombine

## 1. Concept explanation
`thenCombine` combines two independent futures when both complete.

## 2. Problem statement
Fetch two independent values and merge into one response.

## 3. Algorithm intuition
Fan-out two futures, thenCombine to build the final DTO.

## 4. Java 8 implementation
```java
import java.util.concurrent.*;

public class ThenCombineDemo {
    public static void main(String[] args) {
        CompletableFuture<Integer> a = CompletableFuture.completedFuture(40);
        CompletableFuture<Integer> b = CompletableFuture.completedFuture(2);
        CompletableFuture<Integer> c = a.thenCombine(b, Integer::sum);
        System.out.println(c.join());
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
- Input: a=40, b=2

## 7. Execution steps
- Create futures
- thenCombine(sum)
- join

## 8. Output
- Output: 42

## 9. Time and space complexity
- N/A (concept)

## 10. Enterprise relevance
Used for aggregating data from multiple services in parallel.

## 11. Interview discussion points
- thenCombine vs allOf
- failure propagation

## 12. Best practices
- Use timeouts
- Limit concurrency
- Handle partial failures
