# groupingBy

## 1. Concept explanation
`groupingBy` groups elements by a classifier function and optionally applies a downstream collector.

## 2. Problem statement
Group orders by customerId and count orders per customer.

## 3. Algorithm intuition
Use downstream collectors (`counting`, `mapping`, `summingInt`) to avoid multiple passes.

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

public class GroupingByDemo {
    static class Order { final String customer; final int cents; Order(String c, int s){ customer=c; cents=s; } }
    public static void main(String[] args) {
        List<Order> orders = Arrays.asList(new Order("c1", 500), new Order("c1", 700), new Order("c2", 100));
        Map<String, Long> counts = orders.stream()
                .collect(Collectors.groupingBy(o -> o.customer, Collectors.counting()));
        System.out.println(counts);
    }
}
```

## 6. Sample input
- Input: [(c1,500),(c1,700),(c2,100)]

## 7. Execution steps
- Classify by customer
- Downstream counting
- Collect

## 8. Output
- Output: {c1=2, c2=1}

## 9. Time and space complexity
- Time: O(n)
- Space: O(n)

## 10. Enterprise relevance
Used in reporting and analytics endpoints. For huge datasets, prefer DB-side group-by.

## 11. Interview discussion points
- groupingBy vs groupingByConcurrent
- downstream collectors

## 12. Best practices
- Use downstream collectors
- Avoid grouping huge streams in memory
