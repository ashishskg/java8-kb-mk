# Synchronization

## 1. Concept explanation
Synchronization ensures mutual exclusion and establishes *happens-before* relationships so threads see consistent memory updates.

In Java, `synchronized` uses an intrinsic monitor lock on an object.

## 2. Problem statement
Update a shared counter from multiple threads and get the correct final result.

## 3. Algorithm intuition
Without synchronization, increments can be lost. With synchronization, the critical section is protected.

## 4. Java 8 implementation
```java
public class SyncCounter {
    static class Counter {
        private int x = 0;
        synchronized void inc() { x++; }
        synchronized int get() { return x; }
    }

    public static void main(String[] args) throws Exception {
        Counter c = new Counter();
        Thread t1 = new Thread(() -> { for (int i = 0; i < 10000; i++) c.inc(); });
        Thread t2 = new Thread(() -> { for (int i = 0; i < 10000; i++) c.inc(); });
        t1.start();
        t2.start();
        t1.join();
        t2.join();
        System.out.println(c.get());
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
- Input: two threads, each inc 10000 times

## 7. Execution steps
- Enter synchronized inc
- Prevent lost updates
- Join threads
- Print counter

## 8. Output
- Output: 20000

## 9. Time and space complexity
- Time: O(n)
- Space: O(1)

## 10. Enterprise relevance
Incorrect synchronization leads to data corruption, flaky behavior, and hard-to-debug incidents.

## 11. Interview discussion points
- Monitor lock
- Happens-before
- Why ++ is not atomic

## 12. Best practices
- Keep critical sections small
- Prefer higher-level concurrency primitives
- Avoid deadlocks
