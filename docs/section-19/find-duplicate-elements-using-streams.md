# Find Duplicate Elements Using Streams

## 1. Concept explanation
Detect duplicates by tracking seen values and selecting values that appear more than once.

## 2. Problem statement
Given a list, return the set of duplicate elements.

## 3. Algorithm intuition
Maintain a 'seen' set; values that fail to add are duplicates.

## 4. Java 8 implementation
```java
import java.util.*;

public class FindDuplicatesLoop {
    public static void main(String[] args) {
        List<Integer> xs = Arrays.asList(1,2,2,3,3,3);
        Set<Integer> seen = new HashSet<>();
        Set<Integer> dup = new HashSet<>();
        for (int x : xs) {
            if (!seen.add(x)) dup.add(x);
        }
        System.out.println(dup);
    }
}
```

## 5. Stream API implementation
```java
import java.util.*;
import java.util.stream.*;

public class FindDuplicatesStream {
    public static void main(String[] args) {
        List<Integer> xs = Arrays.asList(1,2,2,3,3,3);
        Set<Integer> seen = new HashSet<>();
        Set<Integer> dup = xs.stream().filter(x -> !seen.add(x)).collect(Collectors.toSet());
        System.out.println(dup);
    }
}
```

## 6. Sample input
- Input: [1,2,2,3,3,3]

## 7. Execution steps
- Track seen
- Filter those that repeat
- Collect to set

## 8. Output
- Output: [2, 3] (order may vary)

## 9. Time and space complexity
- Time: O(n)
- Space: O(n)

## 10. Enterprise relevance
Useful for dedupe in ingestion; note this stream approach uses side effects and is not parallel-safe.

## 11. Interview discussion points
- Side effects in streams
- Parallel stream safety

## 12. Best practices
- Prefer groupingBy/counting for pure approach
- Keep it sequential
