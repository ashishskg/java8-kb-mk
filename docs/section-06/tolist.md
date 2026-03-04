# toList

## 1. Concept explanation
`Collectors.toList()` accumulates elements into a List (not guaranteed to be mutable/ArrayList).

## 2. Problem statement
Build a list of normalized emails from a list of raw inputs.

## 3. Algorithm intuition
Use `map` for normalization and `collect(toList())` to materialize results.

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

public class ToListDemo {
    public static void main(String[] args) {
        List<String> raw = Arrays.asList(" A@x.com ", "", "b@x.com");
        List<String> emails = raw.stream()
                .map(String::trim)
                .map(String::toLowerCase)
                .filter(s -> !s.isEmpty())
                .collect(Collectors.toList());
        System.out.println(emails);
    }
}
```

## 6. Sample input
- Input: [" A@x.com ", "", "b@x.com"]

## 7. Execution steps
- Trim/lowercase
- Filter empty
- Collect to list

## 8. Output
- Output: [a@x.com, b@x.com]

## 9. Time and space complexity
- Time: O(n)
- Space: O(n)

## 10. Enterprise relevance
Used for response shaping; beware collecting extremely large streams (prefer paging).

## 11. Interview discussion points
- toList vs toCollection
- mutability guarantees

## 12. Best practices
- Prefer immutable at API boundaries
- Don’t assume ArrayList
