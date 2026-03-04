# Optional API

## 1. Concept explanation
Optional makes absence explicit for return values and reduces null-related bugs.

Guidance: return Optional, avoid Optional fields/serialization, and avoid `get()` without a presence check.

## 2. Problem statement
Model missing data at service boundaries (e.g., user lookup) without returning null.

## 3. Algorithm intuition
Use `map` to transform present values, `flatMap` to avoid nested Optional, and `orElseGet` for lazy defaults.

In Java 8, when converting `List<Optional<T>>` to `List<T>`, you typically filter+get; avoid `get()` without checking presence.

## 4. Java 8 implementation
```java
import java.util.*;

public class OptionalDemo {
    static Optional<String> email(String id) {
        return "u1".equals(id) ? Optional.of("u1@example.com") : Optional.empty();
    }
    public static void main(String[] args) {
        System.out.println(email("u2").orElse("unknown"));
    }
}
```

## 5. Stream API implementation
```java
import java.util.*;
import java.util.stream.*;

public class OptionalStream {
    public static void main(String[] args) {
        List<Optional<Integer>> xs = Arrays.asList(Optional.of(1), Optional.empty(), Optional.of(3));
        List<Integer> out = xs.stream().filter(Optional::isPresent).map(Optional::get).collect(Collectors.toList());
        System.out.println(out);
    }
}
```

## 6. Sample input
- Input: userId = u2
- Input: xs = [Optional(1), Optional.empty, Optional(3)]

## 7. Execution steps
- Lookup returns Optional.empty for missing user
- Apply `orElse` at boundary for default value
- Filter present optionals and unwrap

## 8. Output
- Output: unknown
- Output: [1, 3]

## 9. Time and space complexity
- Time: O(1)
- Space: O(1)

## 10. Enterprise relevance
Reduces NPEs and clarifies service contracts; improves API documentation and caller behavior.

## 11. Interview discussion points
- orElse vs orElseGet
- Optional.map vs flatMap
- Optional in fields?

## 12. Best practices
- Return Optional
- Prefer orElseGet for expensive defaults
- Avoid Optional.get
