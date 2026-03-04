# Thread Lifecycle

## 1. Concept explanation
A thread moves through states like NEW -> RUNNABLE -> (BLOCKED/WAITING/TIMED_WAITING) -> TERMINATED.

In practice, you use `start()`, coordinate with `join()`, and synchronize via locks/monitors/conditions.

## 2. Problem statement
Observe a thread state before start and after completion deterministically.

## 3. Algorithm intuition
`getState()` is a snapshot; the thread may move between states quickly.

## 4. Java 8 implementation
```java
public class ThreadLifecycleDemo {
    public static void main(String[] args) throws Exception {
        Thread t = new Thread(() -> System.out.println("work"));
        System.out.println(t.getState()); // NEW
        t.start();
        t.join();
        System.out.println(t.getState()); // TERMINATED
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
- Input: create thread, start, join

## 7. Execution steps
- Create thread (NEW)
- Start
- Join
- Observe TERMINATED

## 8. Output
- Output: NEW
- Output: work
- Output: TERMINATED

## 9. Time and space complexity
- Time: O(1)
- Space: O(1)

## 10. Enterprise relevance
Understanding lifecycle helps debug stuck threads, deadlocks, and slowdowns in production.

## 11. Interview discussion points
- Difference between RUNNABLE and RUNNING
- BLOCKED vs WAITING
- join semantics

## 12. Best practices
- Name threads
- Avoid creating threads per request
- Use executors
