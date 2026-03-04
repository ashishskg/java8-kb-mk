# Event Driven Processing

## 1. Concept explanation
Event-driven systems process messages asynchronously (queues/streams) with handlers and retries.

## 2. Problem statement
Simulate a simple event queue and process events deterministically.

## 3. Algorithm intuition
Decouple producers and consumers; ensure idempotent handling and ordering guarantees where required.

## 4. Java 8 implementation
```java
import java.util.*;

public class EventDriven {
    public static void main(String[] args) {
        Queue<String> q = new ArrayDeque<>();
        q.add("E1");
        q.add("E2");
        while (!q.isEmpty()) {
            String e = q.remove();
            System.out.println("handled:" + e);
        }
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
- Input: queue=["E1","E2"]

## 7. Execution steps
- Enqueue events
- Dequeue
- Handle

## 8. Output
- Output: handled:E1
- Output: handled:E2

## 9. Time and space complexity
- Time: O(n)
- Space: O(n)

## 10. Enterprise relevance
Real implementations use Kafka/Rabbit/SQS. Key concerns: ordering, retries, DLQ, and idempotency.

## 11. Interview discussion points
- At-least-once delivery
- Idempotent consumers
- Ordering per key

## 12. Best practices
- Use idempotency keys
- Add DLQ
- Instrument lag and failure rate
