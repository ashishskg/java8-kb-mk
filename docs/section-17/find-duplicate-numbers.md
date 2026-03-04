# Find Duplicate Numbers

## 1. Concept explanation
Detect duplicates in an array. Approach depends on constraints (range, memory, modify array allowed).

## 2. Problem statement
Given array a, return any duplicate value if present.

## 3. Algorithm intuition
Use a HashSet to track seen values in O(n) time.

## 4. Java 8 implementation
```java
import java.util.*;

public class FindDuplicate {
    public static Integer find(int[] a) {
        Set<Integer> seen = new HashSet<>();
        for (int x : a) {
            if (!seen.add(x)) return x;
        }
        return null;
    }

    public static void main(String[] args) {
        int[] a = {1,3,4,2,2};
        System.out.println(find(a));
    }
}
```

## 5. Stream API implementation
```java
import java.util.*;
import java.util.stream.*;

public class FindDuplicateStream {
    public static void main(String[] args) {
        List<Integer> xs = Arrays.asList(1,3,4,2,2);
        Set<Integer> seen = new HashSet<>();
        Optional<Integer> dup = xs.stream().filter(x -> !seen.add(x)).findFirst();
        System.out.println(dup.orElse(null));
    }
}
```

## 6. Sample input
- Input: [1,3,4,2,2]

## 7. Execution steps
- Track seen in set
- First value that cannot be added is duplicate

## 8. Output
- Output: 2
- Output(stream): 2

## 9. Time and space complexity
- Time: O(n)
- Space: O(n)

## 10. Enterprise relevance
Used in idempotency checks, deduping event ids, and detecting bad data in ingestion.

## 11. Interview discussion points
- Memory trade-off
- Can you do O(1) space? (Floyd's cycle with constraints)

## 12. Best practices
- Clarify constraints
- Prefer set unless memory is constrained
