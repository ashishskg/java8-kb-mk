# Parallel API Calls

## 1. Concept explanation
Run independent remote calls concurrently and combine results (fan-out/fan-in).

## 2. Problem statement
Call two independent services in parallel and build a combined response.

## 3. Algorithm intuition
Use CompletableFuture.supplyAsync on a bounded executor, thenCombine/allOf to merge.

## 4. Java 8 implementation
```java
import java.util.concurrent.*;

public class ParallelApiCalls {
    static String serviceA() { return "A"; }
    static String serviceB() { return "B"; }

    public static void main(String[] args) {
        ExecutorService es = Executors.newFixedThreadPool(2);
        try {
            CompletableFuture<String> a = CompletableFuture.supplyAsync(ParallelApiCalls::serviceA, es);
            CompletableFuture<String> b = CompletableFuture.supplyAsync(ParallelApiCalls::serviceB, es);
            String out = a.thenCombine(b, (x, y) -> x + y).join();
            System.out.println(out);
        } finally {
            es.shutdown();
        }
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
- Input: serviceA returns A; serviceB returns B

## 7. Execution steps
- Create bounded executor
- Run supplyAsync for each call
- thenCombine
- join

## 8. Output
- Output: AB

## 9. Time and space complexity
- Latency: ~max(latA, latB) (idealized)
- Work: sum of calls

## 10. Enterprise relevance
Core pattern for API aggregators/BFFs. Must add timeouts, retries, bulkheads, and circuit breakers.

## 11. Interview discussion points
- Fan-out/fan-in
- Timeouts
- Thread pool isolation

## 12. Best practices
- Use explicit executors
- Add timeouts
- Limit concurrency
- Avoid blocking inside stages
