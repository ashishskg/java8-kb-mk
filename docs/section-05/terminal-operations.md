# Terminal Operations

## 1. Concept explanation
Terminal operations trigger execution: collect, forEach, reduce, count, min/max, findFirst/anyMatch, etc.

## 2. Problem statement
Demonstrate common terminal ops with deterministic outputs.

## 3. Algorithm intuition
Intermediate ops build; terminal ops consume and produce a result or side effect.

## 4. Java 8 implementation
```java
import java.util.*;

public class TerminalOpsLoop {
    public static void main(String[] args) {
        List<Integer> xs = Arrays.asList(1,2,3,4,5);
        // E1 count
        System.out.println("E1=" + xs.size());
        // E2 sum
        int sum = 0; for (int x : xs) sum += x; System.out.println("E2=" + sum);
        // E3 min/max
        int min = Integer.MAX_VALUE, max = Integer.MIN_VALUE;
        for (int x : xs) { if (x < min) min = x; if (x > max) max = x; }
        System.out.println("E3=" + min + "/" + max);
        // E4 findFirst (first even)
        Integer firstEven = null; for (int x : xs) { if (x % 2 == 0) { firstEven = x; break; } }
        System.out.println("E4=" + firstEven);
        // E5 anyMatch
        boolean anyGt4 = false; for (int x : xs) { if (x > 4) { anyGt4 = true; break; } }
        System.out.println("E5=" + anyGt4);
        // E6 collect (to list of strings)
        List<String> s = new ArrayList<>(); for (int x : xs) s.add("v" + x);
        System.out.println("E6=" + s);
    }
}
```

## 5. Stream API implementation
```java
import java.util.*;
import java.util.stream.*;

public class TerminalOpsStream {
    public static void main(String[] args) {
        List<Integer> xs = Arrays.asList(1,2,3,4,5);
        System.out.println("E1=" + xs.stream().count());
        System.out.println("E2=" + xs.stream().mapToInt(x -> x).sum());
        System.out.println("E3=" + xs.stream().min(Integer::compareTo).get() + "/" + xs.stream().max(Integer::compareTo).get());
        System.out.println("E4=" + xs.stream().filter(x -> x % 2 == 0).findFirst().orElse(-1));
        System.out.println("E5=" + xs.stream().anyMatch(x -> x > 4));
        System.out.println("E6=" + xs.stream().map(x -> "v" + x).collect(Collectors.toList()));
    }
}
```

## 6. Sample input
- Input: [1,2,3,4,5]

## 7. Execution steps
- Call a terminal op
- Print results E1..E6

## 8. Output
- Output: E1=5
- Output: E2=15
- Output: E3=1/5
- Output: E4=2
- Output: E5=true
- Output: E6=[v1, v2, v3, v4, v5]

## 9. Time and space complexity
- Most terminals: O(n)
- min/max: O(n)

## 10. Enterprise relevance
Terminal ops determine materialization. Be careful with `forEach` ordering and side effects.

## 11. Interview discussion points
- findFirst vs findAny
- short-circuiting terminals
- collect vs reduce

## 12. Best practices
- Prefer collect for containers
- Use mapToInt for numeric
- Avoid forEach for business logic
