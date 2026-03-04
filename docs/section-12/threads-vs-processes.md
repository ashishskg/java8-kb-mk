# Threads vs Processes

## 1. Concept explanation
A *process* has its own address space (memory isolation). A *thread* is a unit of execution within a process and shares heap memory with other threads in the same process.

Threads are cheaper to create/switch than processes, but require careful synchronization when sharing mutable state.

## 2. Problem statement
Run two tasks concurrently and understand what is shared (heap) vs isolated (process memory).

## 3. Algorithm intuition
Use threads for concurrency inside a JVM process. Use processes/containers for isolation and separate failure domains.

ASCII:
Process: [Heap] shared by Thread-1, Thread-2

## 4. Java 8 implementation
```java
public class ThreadsVsProcesses {
    static class Counter { int x = 0; }

    public static void main(String[] args) throws Exception {
        Counter c = new Counter();
        Thread t1 = new Thread(() -> c.x++);
        Thread t2 = new Thread(() -> c.x++);
        t1.start();
        t2.start();
        t1.join();
        t2.join();
        System.out.println(c.x); // shared heap state
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
- Input: start two threads that increment shared counter once

## 7. Execution steps
- Create shared object
- Start threads
- Join
- Read shared state

## 8. Output
- Output: 2

## 9. Time and space complexity
- Time: O(1)
- Space: O(1)

## 10. Enterprise relevance
Threads are used for request handling and async work. Processes are used for isolation and scaling boundaries.

## 11. Interview discussion points
- What is shared between threads?
- Context switching
- Isolation trade-offs

## 12. Best practices
- Prefer thread pools
- Avoid sharing mutable state
- Use processes for isolation
