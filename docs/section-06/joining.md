# joining

## 1. Concept explanation
`joining` concatenates CharSequences, optionally with delimiter/prefix/suffix.

## 2. Problem statement
Build a CSV string of unique, sorted product codes.

## 3. Algorithm intuition
Combine `distinct`/`sorted` with joining to get deterministic output.

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

public class JoiningDemo {
    public static void main(String[] args) {
        List<String> codes = Arrays.asList("p2", "p1", "p2");
        String csv = codes.stream().distinct().sorted().collect(Collectors.joining(","));
        System.out.println(csv);
    }
}
```

## 6. Sample input
- Input: ["p2","p1","p2"]

## 7. Execution steps
- distinct
- sorted
- joining(',')

## 8. Output
- Output: p1,p2

## 9. Time and space complexity
- Time: O(n log n)
- Space: O(n)

## 10. Enterprise relevance
Useful for logs, cache keys, and export endpoints; beware very large strings.

## 11. Interview discussion points
- joining vs StringBuilder
- ordering and determinism

## 12. Best practices
- Sort for deterministic outputs
- Avoid joining extremely large streams
