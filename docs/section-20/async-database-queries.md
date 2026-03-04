# Async Database Queries

## 1. Concept explanation
Run DB queries asynchronously using dedicated executors (since JDBC is blocking).

## 2. Problem statement
Fetch user and orders concurrently via async wrappers and combine.

## 3. Algorithm intuition
Wrap blocking IO in supplyAsync on a dedicated IO pool to avoid blocking request threads.

## 4. Java 8 implementation
```java
import java.util.concurrent.*;

public class AsyncDbQueries {
    static String fetchUser() { return "user:u1"; }
    static String fetchOrders() { return "orders:2"; }

    public static void main(String[] args) {
        ExecutorService io = Executors.newFixedThreadPool(4);
        try {
            CompletableFuture<String> u = CompletableFuture.supplyAsync(AsyncDbQueries::fetchUser, io);
            CompletableFuture<String> o = CompletableFuture.supplyAsync(AsyncDbQueries::fetchOrders, io);
            String out = u.thenCombine(o, (a,b) -> a + "," + b).join();
            System.out.println(out);
        } finally {
            io.shutdown();
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
- Input: fetchUser->user:u1, fetchOrders->orders:2

## 7. Execution steps
- Use IO pool
- Wrap blocking calls in supplyAsync
- thenCombine
- join

## 8. Output
- Output: user:u1,orders:2

## 9. Time and space complexity
- Latency: ~max(query1, query2) (idealized)

## 10. Enterprise relevance
In real systems consider async DB drivers/reactive stacks, connection pool limits, and backpressure.

## 11. Interview discussion points
- Why JDBC isn't async
- Thread pool sizing
- Connection pool interaction

## 12. Best practices
- Isolate IO pool
- Never block CPU pool
- Propagate MDC/trace context
