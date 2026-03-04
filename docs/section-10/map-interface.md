# Map Interface

## 1. Concept explanation
`Map` stores key->value associations. Keys are unique (as defined by equals/hashCode), values may repeat.

Map is not a Collection: it has different semantics (key-based lookup).

## 2. Problem statement
Count occurrences of items and query by key efficiently.

## 3. Algorithm intuition
Use HashMap for average O(1) get/put; use TreeMap when you need sorted keys.

## 4. Java 8 implementation
```java
import java.util.*;

public class MapBasics {
    public static void main(String[] args) {
        Map<String, Integer> m = new HashMap<>();
        m.put("a", 1);
        m.put("b", 2);
        m.put("a", 9); // overwrite
        System.out.println(m.get("a"));
        System.out.println(m.containsKey("c"));
    }
}
```

## 5. Stream API implementation
```java
import java.util.*;
import java.util.stream.*;

public class MapCountingStream {
    public static void main(String[] args) {
        List<String> xs = Arrays.asList("a", "b", "a");
        Map<String, Long> counts = xs.stream()
                .collect(Collectors.groupingBy(s -> s, Collectors.counting()));
        System.out.println(counts);
    }
}
```

## 6. Sample input
- Input: put a=1, b=2, a=9
- Input: ["a","b","a"]

## 7. Execution steps
- Put values (overwrite on same key)
- Get by key
- Count via groupingBy

## 8. Output
- Output: 9
- Output: false
- Output: {a=2, b=1}

## 9. Time and space complexity
- put/get: O(1) avg for HashMap
- Space: O(n)

## 10. Enterprise relevance
Maps back caches, request-context attributes, aggregations, and indexing in services.

## 11. Interview discussion points
- Key uniqueness
- containsKey vs get==null
- Why Map isn't a Collection

## 12. Best practices
- Use immutable keys
- Be explicit about null values
- Prefer Map API methods (compute/merge)
