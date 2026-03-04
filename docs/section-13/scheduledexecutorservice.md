# ScheduledExecutorService

## 1. Concept explanation
`ScheduledExecutorService` schedules delayed or periodic tasks (better than Timer).

## 2. Problem statement
Run a delayed task and block until it completes.

## 3. Algorithm intuition
Use `schedule` for one-shot delayed tasks; prefer fixed-rate/fixed-delay for periodic tasks.

## 4. Java 8 implementation
```java
import java.util.concurrent.*;

public class ScheduledDemo {
    public static void main(String[] args) throws Exception {
        ScheduledExecutorService ses = Executors.newScheduledThreadPool(1);
        try {
            ScheduledFuture<String> f = ses.schedule(() -> "tick", 10, TimeUnit.MILLISECONDS);
            System.out.println(f.get());
        } finally {
            ses.shutdown();
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
- Input: schedule callable with 10ms delay

## 7. Execution steps
- Create scheduler
- Schedule
- Future.get
- Shutdown

## 8. Output
- Output: tick

## 9. Time and space complexity
- N/A (concept)

## 10. Enterprise relevance
Used for retries, timeouts, cache refresh, and cron-like background tasks.

## 11. Interview discussion points
- Fixed-rate vs fixed-delay
- Timer pitfalls

## 12. Best practices
- Handle exceptions inside tasks
- Use separate pools for long tasks
- Shutdown gracefully
