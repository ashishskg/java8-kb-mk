# reduce

## 1. Concept explanation
`reduce` folds elements into a single value using an associative accumulator.

## 2. Problem statement
Compute common aggregates deterministically and understand when reduce is appropriate.

## 3. Algorithm intuition
Use reduce for associative operations; prefer specialized terminals (sum/min/max) when available.

## 4. Java 8 implementation
```java
import java.util.*;

public class ReduceLoop {
    public static void main(String[] args) {
        int[] a = {1,2,3,4};
        // E1 sum
        int s = 0; for (int x : a) s += x; System.out.println("E1=" + s);
        // E2 product
        int p = 1; for (int x : a) p *= x; System.out.println("E2=" + p);
        // E3 max
        int mx = Integer.MIN_VALUE; for (int x : a) if (x > mx) mx = x; System.out.println("E3=" + mx);
        // E4 concat
        List<String> xs = Arrays.asList("a","b","c");
        String c = ""; for (String x : xs) c += x; System.out.println("E4=" + c);
        // E5 gcd
        int g = 48;
        int[] b = {18, 30};
        for (int x : b) {
            int aa = g, bb = x;
            while (bb != 0) { int t = aa % bb; aa = bb; bb = t; }
            g = aa;
        }
        System.out.println("E5=" + g);
        // E6 set union
        Set<Integer> u = new LinkedHashSet<>(Arrays.asList(1,2));
        for (int x : Arrays.asList(2,3)) u.add(x);
        System.out.println("E6=" + u);
    }
}
```

## 5. Stream API implementation
```java
import java.util.stream.*;
import java.util.*;

public class ReduceStream {
    public static void main(String[] args) {
        int[] a = {1,2,3,4};
        System.out.println("E1=" + IntStream.of(a).reduce(0, Integer::sum));
        System.out.println("E2=" + IntStream.of(a).reduce(1, (acc,x) -> acc * x));
        System.out.println("E3=" + IntStream.of(a).reduce(Integer.MIN_VALUE, Math::max));
        System.out.println("E4=" + Arrays.asList("a","b","c").stream().reduce("", (acc,x) -> acc + x));
        System.out.println("E5=" + IntStream.of(48, 18, 30).reduce((left, right) -> {
            int a1 = left, b1 = right;
            while (b1 != 0) { int t = a1 % b1; a1 = b1; b1 = t; }
            return a1;
        }).getAsInt());
        System.out.println("E6=" + Stream.of(new LinkedHashSet<>(Arrays.asList(1,2)), new LinkedHashSet<>(Arrays.asList(2,3)))
                .reduce(new LinkedHashSet<>(), (acc, s) -> { acc.addAll(s); return acc; }));
    }
}
```

## 6. Sample input
- Input: a=[1,2,3,4]
- Input: xs=["a","b","c"]
- Input: gcd=[48,18,30]

## 7. Execution steps
- Pick associative operation
- Use identity carefully
- Reduce and print E1..E6

## 8. Output
- Output: E1=10
- Output: E2=24
- Output: E3=4
- Output: E4=abc
- Output: E5=6
- Output: E6=[1, 2, 3]

## 9. Time and space complexity
- Time: O(n)
- Space: O(1)

## 10. Enterprise relevance
Reduction is used for totals and metrics; prefer primitive streams to avoid boxing.

## 11. Interview discussion points
- Associativity requirement
- Parallel reduce pitfalls

## 12. Best practices
- Prefer sum()/summingInt when available
- Use collect for mutable reductions
