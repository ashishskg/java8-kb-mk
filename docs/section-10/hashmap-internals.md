# HashMap Internals

## 1. Concept explanation
`HashMap` uses an array of buckets. A key's hash determines the bucket; collisions are handled within the bucket.

In Java 8, heavily-collided buckets may be treeified (converted to a small tree) to improve worst-case performance.

## 2. Problem statement
Explain collisions, resizing, and why hashCode quality matters.

## 3. Algorithm intuition
Average O(1) relies on good hash distribution; resizing rehashes entries when load factor threshold is exceeded.

## 4. Java 8 implementation
```java
import java.util.*;

public class HashMapDemo {
    public static void main(String[] args) {
        Map<String, Integer> m = new HashMap<>();
        m.put("a", 1);
        m.put("b", 2);
        System.out.println(m.get("b"));
        System.out.println(m.size());
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
- Input: put(a,1), put(b,2), get(b)

## 7. Execution steps
- Compute hash
- Locate bucket
- Scan bucket (equals)
- Return value

## 8. Output
- Output: 2
- Output: 2

## 9. Time and space complexity
- Time: O(1) avg, O(n) worst-case (improved in Java 8 with tree bins)
- Space: O(n)

## 10. Enterprise relevance
HashMap performance impacts caches and hot-path lookups; bad keys can cause CPU spikes and GC pressure.

## 11. Interview discussion points
- Load factor and resizing
- Collision resolution
- Why mutable keys are dangerous

## 12. Best practices
- Implement stable hashCode/equals
- Avoid mutable keys
- Consider initial capacity for large maps
