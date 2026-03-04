# supplyAsync

## 1. Concept explanation
`supplyAsync` runs a Supplier asynchronously and completes with a value.

## 2. Problem statement
Run async computation and return a value.

## 3. Algorithm intuition
Use supplyAsync when you produce a value; use an Executor to control threads.

## 4. Java 8 implementation
```java
import java.util.concurrent.*;

public class SupplyAsyncDemo {
    public static void main(String[] args) {
        ExecutorService es = Executors.newFixedThreadPool(1);
        try {
            CompletableFuture<String> cf = CompletableFuture.supplyAsync(() -> "hello", es);
            System.out.println(cf.join());
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
- Input: Supplier returns 'hello'

## 7. Execution steps
- Create executor
- supplyAsync
- join
- shutdown

## 8. Output
- Output: hello

## 9. Time and space complexity
- N/A (concept)

## 10. Enterprise relevance
Use explicit executors to avoid saturating the common pool in application servers.

## 11. Interview discussion points
- Common pool
- Executor overloads

## 12. Best practices
- Always shutdown custom executors
- Keep suppliers fast or isolate them
