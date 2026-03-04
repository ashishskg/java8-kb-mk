# partitioningBy

## 1. Concept explanation
`partitioningBy` splits elements into exactly two groups based on a predicate.

## 2. Problem statement
Partition transactions into fraud-suspected vs normal.

## 3. Algorithm intuition
Use partitioning when the key is boolean; it always returns keys true/false.

## 4. Java 8 implementation
```java
import java.util.*;

public class Example {
    public static void main(String[] args) {
        List<Integer> xs = Arrays.asList(1, 2, 3, 4, 5);
        int sum = 0;
        for (int x : xs) sum += x;
        System.out.println(sum);
    }
}
```

## 5. Stream API implementation
```java
import java.util.*;
import java.util.stream.*;

public class PartitioningDemo {
    public static void main(String[] args) {
        List<Integer> amounts = Arrays.asList(50, 5000, 20);
        Map<Boolean, List<Integer>> parts = amounts.stream()
                .collect(Collectors.partitioningBy(a -> a >= 1000));
        System.out.println(parts);
    }
}
```

## 6. Sample input
- Input: [50, 5000, 20]

## 7. Execution steps
- Apply predicate a>=1000
- Collect into true/false buckets

## 8. Output
- Output: {false=[50, 20], true=[5000]}

## 9. Time and space complexity
- Time: O(n)
- Space: O(n)

## 10. Enterprise relevance
Common in eligibility checks, filtering audit candidates, and risk pipelines.

## 11. Interview discussion points
- partitioningBy vs groupingBy
- downstream collector

## 12. Best practices
- Use downstream collectors to compute counts/totals
- Keep predicate pure
