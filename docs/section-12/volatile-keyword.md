# Volatile Keyword

## 1. Concept explanation
`volatile` provides visibility guarantees: writes to a volatile field by one thread become visible to reads by other threads.

It does *not* make compound actions (like ++ or check-then-act) atomic.

## 2. Problem statement
Safely publish a stop flag so a worker thread can terminate.

## 3. Algorithm intuition
Use volatile for simple state flags; use locks/atomics for compound updates.

## 4. Java 8 implementation
```java
public class VolatileFlag {
    static volatile boolean stop = false;

    public static void main(String[] args) throws Exception {
        Thread worker = new Thread(() -> {
            while (!stop) {
                // busy wait
            }
            System.out.println("stopped");
        });
        worker.start();
        stop = true;
        worker.join();
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
- Input: stop=false then stop=true

## 7. Execution steps
- Worker polls volatile
- Main writes stop=true
- Worker observes and exits

## 8. Output
- Output: stopped

## 9. Time and space complexity
- Time: depends on polling
- Space: O(1)

## 10. Enterprise relevance
Volatile flags are common in shutdown hooks and component lifecycle management.

## 11. Interview discussion points
- Visibility vs atomicity
- Why volatile doesn't fix ++
- Memory barriers (conceptual)

## 12. Best practices
- Avoid busy-wait in production (use interrupts/locks)
- Use Atomic* for counters
- Keep volatile fields simple
