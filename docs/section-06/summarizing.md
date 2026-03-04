# summarizing

## 1. Concept explanation
`summarizingInt/Long/Double` computes count, sum, min, max, average in one pass.

## 2. Problem statement
Compute summary stats for order amounts.

## 3. Algorithm intuition
Use summarizing when you need multiple numeric aggregates without multiple traversals.

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

public class SummarizingDemo {
    public static void main(String[] args) {
        List<Integer> cents = Arrays.asList(100, 200, 700);
        IntSummaryStatistics st = cents.stream().collect(Collectors.summarizingInt(x -> x));
        System.out.println(st.getCount());
        System.out.println(st.getSum());
        System.out.println(st.getMin());
        System.out.println(st.getMax());
        System.out.println(st.getAverage());
    }
}
```

## 6. Sample input
- Input: [100,200,700]

## 7. Execution steps
- Collect summarizingInt
- Read count/sum/min/max/avg

## 8. Output
- Output: count=3
- Output: sum=1000
- Output: min=100
- Output: max=700
- Output: avg=333.3333333333333

## 9. Time and space complexity
- Time: O(n)
- Space: O(1)

## 10. Enterprise relevance
Used in reporting endpoints and dashboards; prefer primitive specializations for performance.

## 11. Interview discussion points
- summingInt vs summarizingInt
- boxing pitfalls

## 12. Best practices
- Use primitive collectors
- Be aware of double precision for averages
