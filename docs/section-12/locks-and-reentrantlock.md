# Locks and ReentrantLock

## 1. Concept explanation
`ReentrantLock` is an explicit lock with features beyond `synchronized` (tryLock, fairness, conditions).

It is reentrant: the same thread can acquire it multiple times.

## 2. Problem statement
Protect a critical section with try/finally to avoid deadlocks on exceptions.

## 3. Algorithm intuition
Always unlock in a finally block; prefer lock-based code when you need tryLock/timeouts/conditions.

## 4. Java 8 implementation
```java
import java.util.concurrent.locks.*;

public class LockCounter {
    static class Counter {
        private final Lock lock = new ReentrantLock();
        private int x = 0;
        void inc() {
            lock.lock();
            try { x++; }
            finally { lock.unlock(); }
        }
        int get() { return x; }
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
- Input: two threads inc 10000 each

## 7. Execution steps
- Acquire lock
- Update shared state
- Unlock in finally
- Join
- Print

## 8. Output
- Output: 20000

## 9. Time and space complexity
- Time: O(n)
- Space: O(1)

## 10. Enterprise relevance
Locks are common in in-memory caches, rate limiters, and shared state. Prefer minimizing lock contention.

## 11. Interview discussion points
- synchronized vs ReentrantLock
- fairness
- tryLock and deadlock avoidance

## 12. Best practices
- Always unlock in finally
- Keep critical sections small
- Prefer lock-free/atomics when possible
