# Frequency Map Using Streams

## 1. Concept explanation
Build a frequency map (value -> count) using Streams.

## 2. Problem statement
Given a list of tokens, build a frequency map.

## 3. Algorithm intuition
groupingBy(identity, counting) is a pure collector approach.

## 4. Java 8 implementation
```java
import java.util.*;

public class FrequencyMapLoop {
    public static void main(String[] args) {
        List<String> xs = Arrays.asList("a", "b", "a");
        Map<String, Long> freq = new LinkedHashMap<>();
        for (String s : xs) {
            freq.put(s, freq.getOrDefault(s, 0L) + 1L);
        }
        System.out.println(freq);
    }
}
```

## 5. Stream API implementation
```java
import java.util.*;
import java.util.stream.*;

public class FrequencyMap {
    public static void main(String[] args) {
        List<String> xs = Arrays.asList("a", "b", "a");
        Map<String, Long> freq = xs.stream().collect(Collectors.groupingBy(s -> s, LinkedHashMap::new, Collectors.counting()));
        System.out.println(freq);
    }
}
```

## 6. Sample input
- Input: ["a","b","a"]

## 7. Execution steps
- groupingBy token
- downstream counting
- Print map

## 8. Output
- Output: {a=2, b=1}

## 9. Time and space complexity
- Time: O(n)
- Space: O(n)

## 10. Enterprise relevance
Foundational for analytics, logs aggregation, and batch metrics.

## 11. Interview discussion points
- groupingBy vs toMap+merge
- LinkedHashMap supplier

## 12. Best practices
- Control key cardinality
- Prefer LinkedHashMap when ordering matters
