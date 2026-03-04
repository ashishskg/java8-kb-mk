# anyOf

## 1. Concept explanation
`anyOf` completes when any future completes (first result wins).

## 2. Problem statement
Return the first successful response (e.g., from two replicas).

## 3. Algorithm intuition
Race two futures and take the fastest; cancel the slower if appropriate.

## 4. Java 8 implementation
```java
import java.util.concurrent.*;

public class AnyOfDemo {
    public static void main(String[] args) {
        CompletableFuture<String> a = CompletableFuture.completedFuture("A");
        CompletableFuture<String> b = CompletableFuture.completedFuture("B");
        Object first = CompletableFuture.anyOf(a, b).join();
        System.out.println(first);
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
- Input: a="A", b="B"

## 7. Execution steps
- Create futures
- anyOf
- join

## 8. Output
- Output: A (or B depending on completion order)

## 9. Time and space complexity
- N/A (concept)

## 10. Enterprise relevance
Useful for hedged requests and replica reads; requires careful cancellation and cost control.

## 11. Interview discussion points
- Type of anyOf
- Cancellation
- first-completes semantics

## 12. Best practices
- Use timeouts
- Cancel losers when possible
- Avoid duplicate side effects
