# runAsync

## 1. Concept explanation
`runAsync` runs a Runnable asynchronously and completes with no value.

## 2. Problem statement
Fire an async side-effect (logging/audit) and wait for completion at boundary.

## 3. Algorithm intuition
Use runAsync for side effects; prefer keeping side effects at edges.

## 4. Java 8 implementation
```java
import java.util.concurrent.*;

public class RunAsyncDemo {
    public static void main(String[] args) {
        CompletableFuture<Void> cf = CompletableFuture.runAsync(() -> System.out.println("audit"));
        cf.join();
        System.out.println("done");
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
- Input: runnable prints audit

## 7. Execution steps
- runAsync
- join
- continue

## 8. Output
- Output: audit
- Output: done

## 9. Time and space complexity
- N/A (concept)

## 10. Enterprise relevance
Useful for async audit trails and background updates, but ensure failures are handled/observed.

## 11. Interview discussion points
- Void CF
- exception propagation

## 12. Best practices
- Observe exceptions
- Avoid fire-and-forget without monitoring
