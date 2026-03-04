# Garbage Collection Basics

## 1. Concept explanation
Garbage collection (GC) reclaims heap memory for objects that are no longer reachable.

Java 8 HotSpot generational GC idea:
- Young gen: many short-lived objects
- Old gen: long-lived objects

ASCII:
[allocate] -> Eden -> (minor GC) -> Survivor -> ... -> Old

## 2. Problem statement
Explain why allocation rate and object lifetime distribution impacts latency.

## 3. Algorithm intuition
Many short-lived allocations cause frequent minor GCs; large old-gen pressure can cause long pauses depending on collector.

## 4. Java 8 implementation
```java
import java.util.*;

public class AllocationPressure {
    public static void main(String[] args) {
        List<byte[]> keep = new ArrayList<>();
        for (int i = 0; i < 1000; i++) {
            // 1MB allocations
            keep.add(new byte[1024 * 1024]);
        }
        System.out.println(keep.size());
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
- Input: allocate 1000 arrays of 1MB

## 7. Execution steps
- Allocate objects
- Keep references so they survive
- Observe GC impact under profiling

## 8. Output
- Output: 1000

## 9. Time and space complexity
- N/A (concept)

## 10. Enterprise relevance
Allocation rate and GC pauses directly affect p99 latency. High-throughput services require controlling allocation and using appropriate collectors/settings.

## 11. Interview discussion points
- Reachability
- Stop-the-world
- Minor vs major GC
- GC roots

## 12. Best practices
- Reduce temporary objects
- Prefer primitives
- Reuse buffers carefully
- Profile before tuning
