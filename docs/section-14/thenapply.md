# thenApply

## 1. Concept explanation
`thenApply` transforms a completed value (T -> U).

## 2. Problem statement
Parse and transform a value in an async pipeline.

## 3. Algorithm intuition
Use thenApply for synchronous mapping; use thenCompose for async flattening.

## 4. Java 8 implementation
```java
import java.util.concurrent.*;

public class ThenApplyDemo {
    public static void main(String[] args) {
        CompletableFuture<Integer> cf = CompletableFuture.supplyAsync(() -> "21")
                .thenApply(Integer::parseInt)
                .thenApply(x -> x * 2);
        System.out.println(cf.join());
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
- Input: "21"

## 7. Execution steps
- supplyAsync
- thenApply parse
- thenApply multiply
- join

## 8. Output
- Output: 42

## 9. Time and space complexity
- N/A (concept)

## 10. Enterprise relevance
Used for decoding responses and mapping DTOs in async client pipelines.

## 11. Interview discussion points
- thenApply vs thenApplyAsync
- Which thread runs it?

## 12. Best practices
- Keep mapping fast
- Use explicit executors for heavy transforms
