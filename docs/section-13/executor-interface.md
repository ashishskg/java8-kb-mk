# Executor Interface

## 1. Concept explanation
`Executor` is the minimal abstraction for running tasks asynchronously via `execute(Runnable)`.

## 2. Problem statement
Decouple task submission from the threading policy.

## 3. Algorithm intuition
Callers submit work; the executor decides how/when to run it (thread-per-task, pool, etc.).

## 4. Java 8 implementation
```java
import java.util.concurrent.*;

public class ExecutorInterfaceDemo {
    public static void main(String[] args) throws Exception {
        Executor ex = command -> new Thread(command).start();
        CountDownLatch latch = new CountDownLatch(1);
        ex.execute(() -> {
            System.out.println("done");
            latch.countDown();
        });
        latch.await();
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
- Input: submit one Runnable

## 7. Execution steps
- Create Executor
- Execute task
- Await latch

## 8. Output
- Output: done

## 9. Time and space complexity
- N/A (concept)

## 10. Enterprise relevance
Executor abstraction enables swapping policies (bounded pools, tracing executors) without changing business logic.

## 11. Interview discussion points
- Executor vs ExecutorService
- Why execute returns void

## 12. Best practices
- Prefer ExecutorService for lifecycle control
- Avoid creating raw threads per task
