# thenCompose

## 1. Concept explanation
`thenCompose` flattens nested futures: T -> CompletionStage<U> becomes CompletionStage<U>.

## 2. Problem statement
Call async step2 that depends on result of step1.

## 3. Algorithm intuition
thenCompose is like flatMap for futures.

## 4. Java 8 implementation
```java
import java.util.concurrent.*;

public class ThenComposeDemo {
    static CompletableFuture<Integer> fetchUserId() {
        return CompletableFuture.completedFuture(7);
    }
    static CompletableFuture<String> fetchEmail(int userId) {
        return CompletableFuture.completedFuture("u" + userId + "@x.com");
    }
    public static void main(String[] args) {
        String email = fetchUserId().thenCompose(ThenComposeDemo::fetchEmail).join();
        System.out.println(email);
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
- Input: userId=7

## 7. Execution steps
- Fetch userId
- thenCompose fetchEmail
- join

## 8. Output
- Output: u7@x.com

## 9. Time and space complexity
- N/A (concept)

## 10. Enterprise relevance
Common for dependent remote calls (user -> profile -> preferences) without blocking.

## 11. Interview discussion points
- thenCompose vs thenApply
- flatMap analogy

## 12. Best practices
- Avoid blocking between stages
- Add timeouts/retries at boundaries
