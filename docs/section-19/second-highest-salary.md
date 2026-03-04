# Second Highest Salary

## 1. Concept explanation
Find the second highest distinct value from a set of salaries.

## 2. Problem statement
Given employee salaries, return the second highest distinct salary.

## 3. Algorithm intuition
Sort distinct salaries descending and skip the first.

## 4. Java 8 implementation
```java
import java.util.*;

public class SecondHighestSalaryLoop {
    public static Integer secondHighest(List<Integer> xs) {
        Set<Integer> set = new HashSet<>(xs);
        List<Integer> vals = new ArrayList<>(set);
        Collections.sort(vals);
        if (vals.size() < 2) return null;
        return vals.get(vals.size() - 2);
    }

    public static void main(String[] args) {
        System.out.println(secondHighest(Arrays.asList(100, 200, 300, 300)));
    }
}
```

## 5. Stream API implementation
```java
import java.util.*;
import java.util.stream.*;

public class SecondHighestSalaryStream {
    public static void main(String[] args) {
        List<Integer> salaries = Arrays.asList(100, 200, 300, 300);
        Integer second = salaries.stream()
                .distinct()
                .sorted(Comparator.reverseOrder())
                .skip(1)
                .findFirst()
                .orElse(null);
        System.out.println(second);
    }
}
```

## 6. Sample input
- Input: [100,200,300,300]

## 7. Execution steps
- distinct
- sort desc
- skip 1
- findFirst

## 8. Output
- Output: 200

## 9. Time and space complexity
- Time: O(n log n)
- Space: O(n)

## 10. Enterprise relevance
Used in compensation reports and analytics; clarify ties and distinctness rules.

## 11. Interview discussion points
- Second highest vs second distinct
- Handling <2 values

## 12. Best practices
- Define behavior for duplicates
- Avoid sorting if you can do single-pass with two max variables
