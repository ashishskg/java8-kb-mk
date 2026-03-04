# ArrayList Internals

## 1. Concept explanation
`ArrayList` is a resizable array. It stores elements in a contiguous `Object[]` and grows when capacity is exceeded.

Key costs:
- get/set: O(1)
- add at end: amortized O(1)
- insert/remove in middle: O(n) due to shifting

## 2. Problem statement
Avoid performance regressions caused by repeated reallocation and shifting.

## 3. Algorithm intuition
Pre-size when you know approximate size; avoid inserting/removing near the front in tight loops.

## 4. Java 8 implementation
```java
import java.util.*;

public class ArrayListGrowth {
    public static void main(String[] args) {
        List<Integer> xs = new ArrayList<>(8); // pre-size
        for (int i = 1; i <= 5; i++) xs.add(i);
        xs.add(0, 99); // shifts elements right
        System.out.println(xs);
    }
}
```

## 5. Stream API implementation
```java
import java.util.*;
import java.util.stream.*;

public class ArrayListCollectors {
    public static void main(String[] args) {
        List<Integer> out = IntStream.rangeClosed(1, 5).boxed().collect(Collectors.toCollection(ArrayList::new));
        System.out.println(out);
    }
}
```

## 6. Sample input
- Input: add 1..5 then add(0,99)

## 7. Execution steps
- Pre-size
- Append elements
- Insert at index (shift)

## 8. Output
- Output: [99, 1, 2, 3, 4, 5]

## 9. Time and space complexity
- add(end): amortized O(1)
- add(index): O(n)
- remove(index): O(n)

## 10. Enterprise relevance
ArrayList dominates typical service code; performance issues often come from accidental O(n^2) inserts/removes.

## 11. Interview discussion points
- Amortized analysis
- Growth factor
- Why shifting is costly

## 12. Best practices
- Pre-size when possible
- Prefer append
- Use ArrayDeque for queue semantics
