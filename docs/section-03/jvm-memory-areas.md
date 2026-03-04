# JVM Memory Areas (Heap, Stack, Metaspace)

## 1. Concept explanation
The JVM divides memory into areas with different lifetimes and ownership:

- Heap: objects/arrays, GC-managed
- Stack (per thread): frames/local variables/return addresses
- Metaspace: class metadata (HotSpot), native memory

ASCII (simplified):
+-------------------------+
| Heap (Young / Old)     |
+-------------------------+
| Metaspace (classes)    |
+-------------------------+
| Thread Stack (per thr) |
+-------------------------+

## 2. Problem statement
Explain where memory goes when you allocate objects, call methods, and load classes.

## 3. Algorithm intuition
Local primitives and references live in stack frames; the objects they reference live on the heap.

Class loading increases Metaspace usage; excessive classloading can exhaust it.

## 4. Java 8 implementation
```java
public class MemoryAreas {
    static int f(int x) {
        int local = x + 1; // stack
        Integer boxed = local; // boxed object on heap
        return boxed;
    }

    public static void main(String[] args) {
        System.out.println(f(41));
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
- Input: x = 41

## 7. Execution steps
- Call f(41) -> new frame on stack
- Allocate Integer -> heap
- Return value

## 8. Output
- Output: 42

## 9. Time and space complexity
- N/A (concept)

## 10. Enterprise relevance
Heap sizing and GC tuning are core production concerns. Metaspace issues appear with dynamic proxies, class reloading, and large frameworks.

## 11. Interview discussion points
- Heap vs stack
- What triggers GC?
- What lives in Metaspace?
- Escape analysis (conceptual)

## 12. Best practices
- Avoid unnecessary allocations in hot paths
- Watch Metaspace with frameworks/proxies
- Use profiling (JFR/jcmd) before tuning
