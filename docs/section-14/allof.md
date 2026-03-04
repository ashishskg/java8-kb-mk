# allOf

## 1. Concept explanation
`allOf` completes when all futures complete (returns CompletableFuture<Void>).

## 2. Problem statement
Wait for multiple async operations and then build a combined result.

## 3. Algorithm intuition
Use allOf for fan-in; read individual results after it completes.

## 4. Java 8 implementation
```java
import java.util.concurrent.*;

public class AllOfDemo {
    public static void main(String[] args) {
        CompletableFuture<Integer> a = CompletableFuture.completedFuture(1);
        CompletableFuture<Integer> b = CompletableFuture.completedFuture(2);
        CompletableFuture<Void> all = CompletableFuture.allOf(a, b);
        all.join();
        System.out.println(a.join() + b.join());
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
- Input: a=1, b=2

## 7. Execution steps
- Create futures
- allOf
- join all
- read results

## 8. Output
- Output: 3

## 9. Time and space complexity
- N/A (concept)

## 10. Enterprise relevance
Used for batching independent downstream calls with a single synchronization point.

## 11. Interview discussion points
- Why allOf returns Void
- Exception behavior

## 12. Best practices
- Avoid blocking inside pipeline
- Handle timeouts
- Propagate exceptions carefully
