# ThreadPoolExecutor

## 1. Concept explanation
`ThreadPoolExecutor` is the configurable implementation behind most executor factories.

Key knobs: corePoolSize, maxPoolSize, keepAliveTime, workQueue, RejectedExecutionHandler.

## 2. Problem statement
Use a bounded queue and observe deterministic completion of submitted tasks.

## 3. Algorithm intuition
Bounded queues and rejection policies protect services from overload (backpressure).

## 4. Java 8 implementation
```java
import java.util.concurrent.*;
import java.util.*;

public class ThreadPoolExecutorDemo {
    public static void main(String[] args) throws Exception {
        ThreadPoolExecutor ex = new ThreadPoolExecutor(
                1, 1,
                0L, TimeUnit.MILLISECONDS,
                new ArrayBlockingQueue<>(10)
        );
        try {
            List<Future<Integer>> fs = new ArrayList<>();
            for (int i = 0; i < 3; i++) {
                final int x = i;
                fs.add(ex.submit(() -> x * 2));
            }
            for (Future<Integer> f : fs) System.out.println(f.get());
        } finally {
            ex.shutdown();
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
- Input: tasks i=0..2 return i*2

## 7. Execution steps
- Create bounded pool
- Submit tasks
- Future.get
- Shutdown

## 8. Output
- Output: 0
- Output: 2
- Output: 4

## 9. Time and space complexity
- N/A (concept)

## 10. Enterprise relevance
Configuring pool sizes/queues is crucial for API servers to avoid OOM and latency collapse under load.

## 11. Interview discussion points
- Work queue types
- Rejection policies
- Core vs max threads

## 12. Best practices
- Use bounded queues
- Instrument queue depth
- Avoid unbounded cached pools
