# parallel streams

## 1. Concept explanation
Parallel streams split work across threads (ForkJoinPool common pool by default).

## 2. Problem statement
Use parallel streams safely: CPU-bound, stateless operations, deterministic outputs.

## 3. Algorithm intuition
Parallelism helps CPU-bound work when operations are associative and have no side effects.

In servers, common-pool contention can hurt tail latency.

## 4. Java 8 implementation
```java
import java.util.*;

public class ParallelNotesLoop {
    public static void main(String[] args) {
        // E1 baseline sum
        long s = 0;
        for (int i = 1; i <= 10; i++) s += i;
        System.out.println("E1=" + s);

        // E2 expensive CPU loop (deterministic)
        long acc = 0;
        for (int i = 1; i <= 5; i++) acc += (long)i * i;
        System.out.println("E2=" + acc);

        // E3 demonstrate why shared mutation is bad
        // (loop version is deterministic; parallel version would be unsafe)
        List<Integer> xs = Arrays.asList(1,2,3,4,5);
        List<Integer> out = new ArrayList<>();
        for (int x : xs) out.add(x * 2);
        System.out.println("E3=" + out);

        // E4 ordering
        System.out.println("E4=" + xs); // encounter order

        // E5 associative reduce example (sum)
        int sum = 0; for (int x : xs) sum += x;
        System.out.println("E5=" + sum);

        // E6 IO-bound should not be parallelized (concept)
        System.out.println("E6=avoid parallel for IO");
    }
}
```

## 5. Stream API implementation
```java
import java.util.*;
import java.util.stream.*;

public class ParallelStreamExamples {
    public static void main(String[] args) {
        // E1 parallel sum (small range for determinism)
        System.out.println("E1=" + LongStream.rangeClosed(1, 10).parallel().sum());

        // E2 parallel map (CPU-ish)
        System.out.println("E2=" + IntStream.rangeClosed(1, 5).parallel().mapToLong(x -> (long)x * x).sum());

        // E3 avoid side effects: use collect not shared list mutation
        List<Integer> xs = Arrays.asList(1,2,3,4,5);
        System.out.println("E3=" + xs.parallelStream().map(x -> x * 2).sorted().collect(Collectors.toList()));

        // E4 ordering: forEach vs forEachOrdered
        String a = IntStream.rangeClosed(1, 5).parallel().mapToObj(String::valueOf).collect(Collectors.joining(""));
        String b = IntStream.rangeClosed(1, 5).parallel().mapToObj(String::valueOf).sequential().collect(Collectors.joining(""));
        System.out.println("E4=" + a + "/" + b);

        // E5 associative reduction safe; non-associative is not
        System.out.println("E5=" + IntStream.rangeClosed(1, 5).parallel().reduce(0, Integer::sum));

        // E6 limit may behave differently with unordered; keep it ordered here
        System.out.println("E6=" + IntStream.rangeClosed(1, 100).parallel().filter(x -> x % 10 == 0).limit(3).boxed().collect(Collectors.toList()));
    }
}
```

## 6. Sample input
- Input: range 1..10
- Input: xs=[1,2,3,4,5]

## 7. Execution steps
- Use parallel only where it helps
- Avoid shared mutation
- Prefer forEachOrdered if you need order

## 8. Output
- Output: E1=55
- Output: E2=55
- Output: E3=[2, 4, 6, 8, 10]
- Output: E5=15
- Output: E6=[10, 20, 30]

## 9. Time and space complexity
- Work: O(n)
- Speedup: depends on cores/data size/overhead

## 10. Enterprise relevance
Parallel streams can harm latency in servers due to shared common pool. Prefer explicit executors for isolation.

## 11. Interview discussion points
- forEach vs forEachOrdered
- Associativity
- Common pool contention

## 12. Best practices
- Measure
- Keep lambdas pure
- Avoid IO in parallel streams
- Use explicit pools in servers
