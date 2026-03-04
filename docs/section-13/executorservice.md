# ExecutorService

## 1. Concept explanation
`ExecutorService` extends Executor with lifecycle (`shutdown`) and task submission returning `Future`.

## 2. Problem statement
Run a Callable task and get its result deterministically.

## 3. Algorithm intuition
Use `submit(Callable)` to get a Future; always shutdown the pool.

## 4. Java 8 implementation
```java
import java.util.concurrent.*;

public class ExecutorServiceDemo {
    public static void main(String[] args) throws Exception {
        ExecutorService es = Executors.newFixedThreadPool(2);
        try {
            Future<Integer> f = es.submit(() -> 40 + 2);
            System.out.println(f.get());
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
- Input: Callable returns 42

## 7. Execution steps
- Create pool
- Submit callable
- Future.get
- Shutdown

## 8. Output
- Output: 42

## 9. Time and space complexity
- N/A (concept)

## 10. Enterprise relevance
Thread pools prevent unbounded thread creation and support graceful shutdowns.

## 11. Interview discussion points
- shutdown vs shutdownNow
- Future.get blocking
- submit vs execute

## 12. Best practices
- Always shutdown
- Use bounded queues
- Set thread names
