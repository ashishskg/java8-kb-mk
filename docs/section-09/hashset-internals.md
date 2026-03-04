# HashSet Internals

## 1. Concept explanation
`HashSet` is backed by a `HashMap` (elements are stored as keys with a dummy value).

Lookup uses hashCode to find a bucket, then equals to resolve collisions.

## 2. Problem statement
Explain collisions and why poor hashCode causes performance regressions.

## 3. Algorithm intuition
If many keys land in the same bucket, operations degrade toward O(n).

## 4. Java 8 implementation
```java
import java.util.*;

public class HashSetDemo {
    public static void main(String[] args) {
        Set<String> s = new HashSet<>();
        s.add("a");
        s.add("a");
        s.add("b");
        System.out.println(s.size());
        System.out.println(s.contains("b"));
    }
}
```

## 5. Stream API implementation
```java
import java.util.*;
import java.util.stream.*;

public class Example {
    public static void main(String[] args) {
        List<Integer> xs = Arrays.asList(1, 2, 3, 4, 5);
        int sumOfEvens = xs.stream().filter(x -> x % 2 == 0).mapToInt(x -> x).sum();
        System.out.println(sumOfEvens);
    }
}
```

## 6. Sample input
- Input: add("a"), add("a"), add("b")

## 7. Execution steps
- Compute hash
- Check bucket
- Use equals to detect duplicate

## 8. Output
- Output: 2
- Output: true

## 9. Time and space complexity
- Time: O(1) avg, O(n) worst-case
- Space: O(n)

## 10. Enterprise relevance
Hot-path caches and dedupe sets rely on good hashing; poor keys can cause latency spikes.

## 11. Interview discussion points
- Collision handling
- Why equals/hashCode matters
- Load factor and resizing

## 12. Best practices
- Implement stable hashCode
- Avoid mutable keys
- Use appropriate initial capacity when large
