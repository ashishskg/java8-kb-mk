# Batch Processing

## 1. Concept explanation
Batch jobs process many records with chunking, retries, and idempotency.

## 2. Problem statement
Process records in chunks and compute an aggregate deterministically.

## 3. Algorithm intuition
Chunk to control memory, and make each chunk idempotent for retries.

## 4. Java 8 implementation
```java
import java.util.*;

public class BatchProcessing {
    static long chunkSum(List<Integer> chunk) {
        long s = 0;
        for (int x : chunk) s += x;
        return s;
    }

    public static void main(String[] args) {
        List<Integer> xs = Arrays.asList(1,2,3,4,5,6);
        int chunkSize = 2;
        long total = 0;
        for (int i = 0; i < xs.size(); i += chunkSize) {
            List<Integer> chunk = xs.subList(i, Math.min(i + chunkSize, xs.size()));
            total += chunkSum(chunk);
        }
        System.out.println(total);
    }
}
```

## 5. Stream API implementation
```java
import java.util.*;
import java.util.stream.*;

public class BatchStreamNote {
    public static void main(String[] args) {
        List<Integer> xs = Arrays.asList(1,2,3,4,5,6);
        long total = xs.stream().mapToLong(x -> x).sum();
        System.out.println(total);
    }
}
```

## 6. Sample input
- Input: xs=[1,2,3,4,5,6], chunkSize=2

## 7. Execution steps
- Split into chunks
- Process chunk
- Accumulate
- Print

## 8. Output
- Output: 21

## 9. Time and space complexity
- Time: O(n)
- Space: O(1) extra

## 10. Enterprise relevance
Batch patterns appear in ETL, reporting, billing, and reprocessing. Correctness needs idempotency and checkpointing.

## 11. Interview discussion points
- Idempotency
- Checkpointing
- Exactly-once vs at-least-once

## 12. Best practices
- Chunk to control memory
- Make handlers idempotent
- Add retries with DLQ strategy
